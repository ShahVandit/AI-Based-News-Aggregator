import React, { useEffect, useState } from "react";
import {
  Backdrop,
  CircularProgress,
  Grid,
  Grow,
  Typography,
} from "@material-ui/core";

import NewsCard from "./NewsCard/NewsCard";
import useStyles from "./styles.js";
// import Backdrop from "@mui/material/Backdrop";
// import CircularProgress from "@mui/material/CircularProgress";
import { Link } from "react-router-dom";
import axios from "axios";

const infoCards = [
  {
    color: "#00838f",
    title: ["Latest News", "ताजा खबर", "તાજા સમાચાર"],
    text: [
      "Give me the latest news",
      "मुझे नवीनतम समाचार दें",
      "મને નવીનતમ સમાચાર આપો",
    ],
    url: "https://api.newscatcherapi.com/v2/latest_headlines?countries=IN&lang=en",
  },
  {
    color: "#1565c0",
    title: [
      "News by Categories",
      "श्रेणियाँ द्वारा समाचार",
      "શ્રેણીઓ દ્વારા સમાચાર",
    ],
    info: [
      {
        English:
          "Business, Entertainment, General, Health, Science, Sports, Technology",
      },
      {
        Hindi:
          "व्यापार, मनोरंजन, सामान्य, स्वास्थ्य, विज्ञान, खेल, प्रौद्योगिकी",
      },
      {
        Gujarati:
          "વ્યવસાય, મનોરંજન, સામાન્ય, આરોગ્ય, વિજ્ઞાન, રમતગમત, ટેકનોલોજી",
      },
    ],
    text: [
      "Give me the latest Business news",
      "मुझे नवीनतम व्यावसायिक समाचार दें",
      "મને નવીનતમ વ્યવસાય સમાચાર આપો",
    ],
    url: "https://api.newscatcherapi.com/v2/latest_headlines?countries=IN&lang=en&topic=business",
  },
  {
    color: "#4527a0",
    title: ["News by Terms", "शर्तें द्वारा समाचार", "શરતો દ્વારા સમાચાર"],
    info: [
      { English: "Bitcoin, PlayStation 5, Smartphones, Donald Trump" },
      { Hindi: "बिटकॉइन, प्लेस्टेशन 5, स्मार्टफोन, डोनाल्ड ट्रम्प" },
      { Gujarati: "બિટકોઇન, પ્લેસ્ટેશન 5, સ્માર્ટફોન, ડોનાલ્ડ ટ્રમ્પ" },
    ],
    text: [
      "What's up with Narendra Modi",
      "क्या हाल है नरेंद्र मोदी का",
      "નરેન્દ્ર મોદી સાથે શું ચાલી રહ્યું છે",
    ],
    url: "https://api.newscatcherapi.com/v2/search?countries=IN&lang=en&q=Smartphones",
  },
  // {
  //   color: "#283593",
  //   title: "News by Sources",
  //   info: "News 18, News 24, Times Of India,NDTV...",
  //   text: "Give me the news from News 18",
  // },
];

const NewsCards = ({
  alanBtnRef,
  articles,
  activeArticle,
  language,
  newsArticles,
  setNewsArticles,
  setDummy,
}) => {
  const classes = useStyles();
  const len = [9, 10, 11, 12];
  const [loading, setLoading] = useState(false);
  const query_lang =
    language == "English" ? "en" : language == "Hindi" ? "hi" : "gu";

  const NEWS_API_KEY = process.env.REACT_APP_CATCHER_KEY;
  const handleUrl = async (urls) => {
    setLoading(true);
    const res = await axios.get(urls, {
      headers: { "x-api-key": NEWS_API_KEY },
    });
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
      setNewsArticles(sres);
      setLoading(false);
      localStorage.setItem("articles", JSON.stringify(sres));
    } else {
      sres = response.data.sort(
        (a1, a2) => new Date(a2.date).getTime() - new Date(a1.date).getTime()
      );
      setNewsArticles(sres);
      setLoading(false);
      // res.data
      localStorage.setItem("articles", JSON.stringify(sres));
    }
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
  if (!articles?.length) {
    return (
      <Grow in>
        <Grid
          className={classes.container}
          container
          alignItems="stretch"
          spacing={3}
          style={{ marginTop: "10rem" }}
        >
          {infoCards.map((infoCard) => (
            <Grid
              onClick={() => handleUrl(infoCard.url)}
              item
              xs={12}
              sm={6}
              md={4}
              lg={4}
              style={{ cursor: "pointer" }}
              className={classes.infoCard}
            >
              <div
                className={classes.card}
                style={{ backgroundColor: infoCard.color }}
              >
                <Typography variant="h5" component="h5">
                  {language === "English"
                    ? infoCard.title[0]
                    : language === "Hindi"
                    ? infoCard.title[1]
                    : infoCard.title[2]}
                </Typography>
                {infoCard.info ? (
                  <Typography variant="h6" component="h6">
                    {/* <strong>{infoCard.title.split(" ")[2]}</strong>: <br /> */}
                    {language === "English"
                      ? infoCard.info[0].English
                      : language === "Hindi"
                      ? infoCard.info[1].Hindi
                      : infoCard.info[2].Gujarati}
                  </Typography>
                ) : null}
                <Typography variant="h6" component="h6">
                  Try saying: <br />{" "}
                  <i>
                    {language === "English"
                      ? infoCard.text[0]
                      : language === "Hindi"
                      ? infoCard.text[1]
                      : infoCard.text[2]}
                  </i>
                </Typography>
              </div>
            </Grid>
          ))}
        </Grid>
      </Grow>
    );
  }

  return (
    <Grow in>
      <Grid
        className={`${classes.container} ${classes.newsCardLength}`}
        container
        alignItems="stretch"
        spacing={3}
      >
        {articles
          .slice(0, len[Math.floor(Math.random() * 5)])
          .map((article, i) => (
            <Grid item xs={12} sm={6} md={4} lg={4} style={{ display: "flex" }}>
              <NewsCard
                alanBtnRef={alanBtnRef}
                language={language}
                activeArticle={activeArticle}
                i={i}
                article={article}
                newsArticles={newsArticles}
                setNewsArticles={setNewsArticles}
              />
            </Grid>
          ))}
      </Grid>
    </Grow>
  );
};

export default NewsCards;
