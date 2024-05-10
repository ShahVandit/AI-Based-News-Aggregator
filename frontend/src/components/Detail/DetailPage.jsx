import React, { useEffect, useState } from "react";
import {
  Card,
  CardActionArea,
  CardMedia,
  Container,
  CardContent,
  Box,
  Button,
  CardActions,
  Typography,
  Tabs,
  Tab,
  AppBar,
  useTheme,
  Backdrop,
  CircularProgress,
} from "@material-ui/core";
import Paper from "@material-ui/core/Paper";

import PropTypes from "prop-types";
import SwipeableViews from "react-swipeable-views";

import useStyles from "./styles";
import Slider from "react-slick";
import Grid from "@material-ui/core/Grid";
import { useHistory, useLocation } from "react-router-dom";
import axios from "axios";
import "./Detail.css";

// tab functionality
function TabPanel(props) {
  const { children, value, index, ...other } = props;

  return (
    <div
      role="tabpanel"
      hidden={value !== index}
      id={`full-width-tabpanel-${index}`}
      aria-labelledby={`full-width-tab-${index}`}
      {...other}
    >
      {value === index && (
        <Box p={3}>
          <Typography>{children}</Typography>
        </Box>
      )}
    </div>
  );
}

TabPanel.propTypes = {
  children: PropTypes.node,
  index: PropTypes.any.isRequired,
  value: PropTypes.any.isRequired,
};

function a11yProps(index) {
  return {
    id: `full-width-tab-${index}`,
    "aria-controls": `full-width-tabpanel-${index}`,
  };
}

const DetailPage = () => {
  const classes = useStyles();
  var settings = {
    dots: false,
    infinite: false,
    speed: 500,
    slidesToShow: 4,
    slidesToScroll: 1,
    initialSlide: 0,
    arrows: false,
    swipeToSlide: true,
    responsive: [
      {
        breakpoint: 1024,
        settings: {
          slidesToShow: 3,
          slidesToScroll: 1,
          infinite: true,
          dots: true,
          arrows: false,
          swipeToSlide: true,
        },
      },
      {
        breakpoint: 600,
        settings: {
          slidesToShow: 2,
          slidesToScroll: 1,
          initialSlide: 2,
          arrows: false,
          swipeToSlide: true,
          infinite: true,
          dots: true,
        },
      },
      {
        breakpoint: 480,
        settings: {
          slidesToShow: 1,
          slidesToScroll: 1,
          infinite: true,
          arrows: false,
          swipeToSlide: true,
          dots: true,
        },
      },
    ],
  };
  var settings2 = {
    dots: false,
    infinite: true,
    speed: 500,
    slidesToShow: 1,
    slidesToScroll: 1,
    initialSlide: 0,
    arrows: true,
    swipeToSlide: true,
    responsive: [
      {
        breakpoint: 1024,
        settings: {
          slidesToShow: 1,
          slidesToScroll: 1,
          infinite: true,
          dots: true,
          arrows: false,
          swipeToSlide: true,
        },
      },
      {
        breakpoint: 600,
        settings: {
          slidesToShow: 1,
          slidesToScroll: 1,
          initialSlide: 2,
          arrows: false,
          swipeToSlide: true,
          infinite: true,
          dots: true,
        },
      },
      {
        breakpoint: 480,
        settings: {
          slidesToShow: 1,
          slidesToScroll: 1,
          infinite: true,
          arrows: false,
          swipeToSlide: true,
          dots: true,
        },
      },
    ],
  };
  const NEWS_API_KEY = process.env.REACT_APP_CATCHER_KEY;

  const location = useLocation();
  // console.log(location.state);
  const [summ, setSumm] = useState("");

  const config = {
    headers: {
      "x-api-key": NEWS_API_KEY,
    },
  };

  const article = location.state?.article || {};
  const newsArticles = location.state?.newsArticles || [];
  const language = JSON.parse(localStorage.getItem("language"));
  // const summ = location.state?.summ || "";
  // const setSumm = location.state?.setSumm;
  // const { article = {}, newsArticles = [] } = location.state;

  const [recommendArticles, setRecommendArticles] = useState([]);
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    const summarization = async () => {
      const res = await axios.post("http://127.0.0.1:8000/summarize/", {
        language: language,
        content: article.content,
      });
      console.log(res.data);
      setSumm(res.data);
    };
    summarization();
  }, [language, article.content]);

  const substr = (summary) => {
    return summary.substring(0, 60) + "...";
  };

  const findRecommendedNews = async () => {
    const response = await axios.post("http://127.0.0.1:8000/recommendation/", {
      currentArticle: article,
      articles: JSON.parse(localStorage.getItem("articles")) || newsArticles,
    });
    // console.log(JSON.parse(response.data[0]));
    // setRecommendArticles(
    var uni = new Set();
    response.data.map((articl) => uni.add(JSON.parse(articl)));
    setRecommendArticles(Array.from(uni));
    // );
  };

  useEffect(() => {
    findRecommendedNews();
  }, [article?.title]);

  const [mobile, setMobile] = useState(false);
  function handleWindowSizeChange() {
    let width = window.innerWidth;

    if (width <= 960) {
      setMobile(true);
    } else {
      setMobile(false);
    }
  }
  useEffect(() => {
    window.addEventListener("resize", handleWindowSizeChange);
    return () => {
      window.removeEventListener("resize", handleWindowSizeChange);
    };
  });

  const theme = useTheme();
  const [value, setValue] = React.useState(0);

  const handleChange = (event, newValue) => {
    setValue(newValue);
  };
  const history = useHistory();

  const handleChangeIndex = (index) => {
    setValue(index);
  };
  const handleUrl = async (topics) => {
    setLoading(true);
    const res = await axios.get(
      `https://api.newscatcherapi.com/v2/latest_headlines?countries=IN&lang=en&topic=${topics}`,
      {
        headers: { "x-api-key": NEWS_API_KEY },
      }
    );
    var sres = [];
    const response = await axios.post(`http://127.0.0.1:8000/scrape/`, {
      articles: res.data.articles.slice(
        0,
        Math.min(20, res.data.articles.length)
      ),
    });
    if (language !== "English") {
      const responsee = await axios.post("http://127.0.0.1:8000/translate/", {
        articles: response.data,
        language: language,
        cur_lang: "English",
      });
      sres = responsee.data.sort(
        (a1, a2) => new Date(a2.date).getTime() - new Date(a1.date).getTime()
      );
      setLoading(false);
      localStorage.setItem("articles", JSON.stringify(sres));
    } else {
      sres = response.data.sort(
        (a1, a2) => new Date(a2.date).getTime() - new Date(a1.date).getTime()
      );
      setLoading(false);
      // res.data
      localStorage.setItem("articles", JSON.stringify(sres));
    }
    history.push("/");
  };

  const handleArticle = (singleArticle, i) => {
    console.log("Raj" + i);
    history.push({
      pathname: `/${i}`,
      state: { article: singleArticle, newsArticles: newsArticles },
    });
    window.scroll(0, 0);
  };
  if (loading) {
    return (
      <>
        <Backdrop
          sx={{
            color: "#999",
            zIndex: (theme) => theme.zIndex.drawer + 1,
          }}
          open
        >
          <CircularProgress color="inherit" />
        </Backdrop>
      </>
    );
  }
  return (
    <>
      <div className={classes.marginTop}>
        <Container>
          <Slider {...settings}>
            <div>
              <Box className={classes.box}>
                <Card
                  variant="outlined"
                  style={{ borderRadius: "10px", cursor: "pointer" }}
                  onClick={() => handleUrl("news")}
                >
                  <div
                    className={classes.card}
                    style={{
                      background: `linear-gradient(
        to bottom,
        rgba(0, 0, 0, 0) 0%,
        rgba(0, 0, 0, 1) 100%
      ),
      url('https://assets.nflxext.com/ffe/siteui/vlv3/a795ee10-8c6d-467c-8159-254be2b69013/c08e0e8a-d28f-4d82-bf93-0a9531b58a6d/IN-en-20220912-popsignuptwoweeks-perspective_alpha_website_large.jpg')`,
                    }}
                  >
                    <Typography
                      variant="h5"
                      component="h2"
                      style={{ fontSize: "50px", wordBreak: "break-all" }}
                    >
                      {language === "English"
                        ? "Top Stories"
                        : language === "Hindi"
                        ? "शीर्ष आलेख"
                        : "ટોચની વાર્તાઓ"}
                    </Typography>
                  </div>
                </Card>
              </Box>
            </div>
            <div>
              <Box className={classes.box}>
                <Card
                  variant="outlined"
                  style={{ borderRadius: "10px", cursor: "pointer" }}
                  onClick={() => handleUrl("sport")}
                >
                  <div
                    className={classes.card}
                    style={{
                      background: `linear-gradient(
        to bottom,
        rgba(0, 0, 0, 0) 0%,
        rgba(0, 0, 0, 1) 100%
      ),
      url('https://ijclp.com/wp-content/uploads/2021/10/Sports-1024x576.jpg')`,
                    }}
                  >
                    <Typography
                      variant="h5"
                      component="h2"
                      style={{ fontSize: "50px", wordBreak: "break-all" }}
                    >
                      {language === "English"
                        ? "Sports"
                        : language === "Hindi"
                        ? "खेल"
                        : "રમતગમત"}
                    </Typography>
                  </div>
                </Card>
              </Box>
            </div>
            <div>
              <Box className={classes.box}>
                <Card
                  variant="outlined"
                  style={{ borderRadius: "10px", cursor: "pointer" }}
                  onClick={() => handleUrl("politics")}
                >
                  <div
                    className={classes.card}
                    style={{
                      background: `linear-gradient(
        to bottom,
        rgba(0, 0, 0, 0) 0%,
        rgba(0, 0, 0, 1) 100%
      ),
      url('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSFlxgjcpUlkOXxOo2sLV1Ms0zpH_K0q0GVFw&usqp=CAU')`,
                    }}
                  >
                    <Typography
                      variant="h5"
                      component="h2"
                      style={{ fontSize: "50px", wordBreak: "break-all" }}
                    >
                      {language === "English"
                        ? "Politics"
                        : language === "Hindi"
                        ? "राजनीति"
                        : "રાજકારણ"}
                    </Typography>
                  </div>
                </Card>
              </Box>
            </div>
            <div>
              <Box className={classes.box}>
                <Card
                  variant="outlined"
                  style={{ borderRadius: "10px", cursor: "pointer" }}
                  onClick={() => handleUrl("business")}
                >
                  <div
                    className={classes.card}
                    style={{
                      background: `linear-gradient(
        to bottom,
        rgba(0, 0, 0, 0) 0%,
        rgba(0, 0, 0, 1) 100%
      ),
      url('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTNev3rPr9u4_X3syU2UPRX3ueCjQ6_8vBiMHRAGmfAXERpp_fXhoDW0Eg9yXIAC2JhRfc&usqp=CAU')`,
                      objectFit: "contain",
                    }}
                  >
                    <Typography
                      variant="h5"
                      component="h2"
                      style={{ fontSize: "50px", wordBreak: "break-all" }}
                    >
                      {language === "English"
                        ? "Business"
                        : language === "Hindi"
                        ? "व्यवसाय"
                        : "બિઝનેસ"}
                    </Typography>
                  </div>
                </Card>
              </Box>
            </div>
          </Slider>
        </Container>
      </div>
      <div className={classes.dlogoContainer}>
        {newsArticles?.length ? (
          <div
            className={classes.dinfoContainer}
            style={{ marginTop: "2rem", marginBottom: "2rem" }}
          >
            {language === "English" && (
              <div className={classes.dcard}>
                <Typography variant="h5" component="h2">
                  Try saying: <br />
                  <br />
                  Reads News Summary for me.
                </Typography>
              </div>
            )}
            {language === "English" && (
              <div className={classes.dcard}>
                <Typography variant="h5" component="h2">
                  Try saying: <br />
                  <br />
                  Read full article for me.
                </Typography>
              </div>
            )}
          </div>
        ) : null}
      </div>
      <div className={classes.marginBottom}>
        <Container>
          <Grid container spacing={2}>
            <Grid item xs={12} sm={12} md={8} lg={9}>
              <div>
                <h1>{article?.title}</h1>
              </div>
              <div>
                <img
                  className={classes.image}
                  src={
                    article?.media ||
                    "https://www.industry.gov.au/sites/default/files/August%202018/image/news-placeholder-738.png"
                  }
                />
              </div>

              <div className={classes.roots}>
                <AppBar position="static" color="default">
                  <Tabs
                    value={value}
                    onChange={handleChange}
                    indicatorColor="primary"
                    textColor="primary"
                    variant="fullWidth"
                    aria-label="full width tabs example"
                  >
                    <Tab label="Full Article" {...a11yProps(0)} />
                    <Tab label="Summarised Article" {...a11yProps(1)} />
                  </Tabs>
                </AppBar>
                <SwipeableViews
                  axis={theme.direction === "rtl" ? "x-reverse" : "x"}
                  index={value}
                  onChangeIndex={handleChangeIndex}
                >
                  <TabPanel value={value} index={0} dir={theme.direction}>
                    {article?.content}
                  </TabPanel>
                  <TabPanel value={value} index={1} dir={theme.direction}>
                    {summ}
                  </TabPanel>
                </SwipeableViews>
              </div>

              <div className={classes.authorBox} style={{ marginTop: "1rem" }}>
                <div>
                  <h2>Author: ${article.author}`</h2>

                  <p style={{ fontSize: "20px", fontWeight: "thin" }}>
                    {article?.excerpt}
                  </p>
                </div>
                <div className={classes.right}>
                  <h2>
                    Published At:<br></br>
                    {new Date(article?.published_date).toDateString()}
                  </h2>
                </div>
              </div>
            </Grid>

            <Grid
              item
              xs={12}
              sm={12}
              md={4}
              lg={3}
              className={classes.recommendation}
            >
              {mobile && (
                <>
                  <Slider {...settings}>
                    {recommendArticles &&
                      recommendArticles.map((singleArticle, i) =>
                        singleArticle.title !== article?.title ? (
                          <div
                            style={{ cursor: "pointer" }}
                            onClick={() => handleArticle(singleArticle, i)}
                          >
                            <Box key={i} className={classes.recommendation_box}>
                              {console.log("Bhavya " + i)}
                              <Card>
                                <CardActionArea>
                                  <CardMedia
                                    className={classes.imgs}
                                    component="img"
                                    alt="Contemplative Reptile"
                                    image={
                                      `${singleArticle.media}` ||
                                      "https://english.cdn.zeenews.com/sites/default/files/styles/zm_700x400/public/2022/12/05/1125917-google-file.jpg"
                                    }
                                    title="Contemplative Reptile"
                                  />
                                  <CardContent>
                                    <Typography
                                      variant="body2"
                                      color="textSecondary"
                                      component="p"
                                    >
                                      {substr(singleArticle.content)}
                                    </Typography>
                                  </CardContent>
                                </CardActionArea>
                                <CardActions className={classes.flex_center}>
                                  <Button>
                                    {new Date(
                                      singleArticle.date
                                    ).toDateString()}
                                  </Button>
                                  <Button>{singleArticle.author}</Button>
                                  <div className={classes.flex_center}>
                                    <h3 style={{ width: "60%" }}>
                                      {new Date(
                                        singleArticle?.published_date
                                      ).toDateString()}
                                    </h3>
                                    <h3 style={{ width: "40%" }}>
                                      {singleArticle.author}
                                    </h3>
                                  </div>
                                </CardActions>
                              </Card>
                            </Box>
                          </div>
                        ) : (
                          <></>
                        )
                      )}
                  </Slider>
                </>
              )}
              {!mobile && (
                <>
                  <Box className={`${classes.author_box} ${classes.scrollBar}`}>
                    {recommendArticles &&
                      recommendArticles.map((singleArticle, index) =>
                        singleArticle.title !== article?.title ? (
                          <Paper
                            style={{ cursor: "pointer" }}
                            onClick={() => handleArticle(singleArticle)}
                            key={index}
                            elevation={5}
                            className={classes.paper}
                          >
                            <Card
                              className={classes.root}
                              style={{ marginBottom: "1rem" }}
                            >
                              <CardMedia
                                className={classes.cover}
                                image={
                                  `${singleArticle.media}` ||
                                  "https://english.cdn.zeenews.com/sites/default/files/styles/zm_700x400/public/2022/12/05/1125917-google-file.jpg"
                                }
                                title="Live from space album cover"
                              />
                              <div className={classes.details}>
                                <div className={classes.content}>
                                  <p style={{ fontColor: "black !important" }}>
                                    {substr(singleArticle.content)}
                                  </p>
                                  <div className={classes.flex_center}>
                                    <h3
                                      style={{
                                        width: "60%",
                                        fontWeight: "bold !important",
                                      }}
                                    >
                                      {new Date(
                                        singleArticle.published_date
                                      ).toDateString()}
                                    </h3>
                                    <h3
                                      style={{
                                        width: "40%",
                                        fontWeight: "bold !important",
                                      }}
                                    >
                                      {singleArticle.author}`
                                    </h3>
                                  </div>
                                </div>
                              </div>
                            </Card>
                          </Paper>
                        ) : (
                          <></>
                        )
                      )}
                  </Box>
                </>
              )}
            </Grid>
          </Grid>
        </Container>
      </div>
    </>
  );
};

export default DetailPage;
