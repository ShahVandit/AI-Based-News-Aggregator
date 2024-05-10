import React, { useState, useEffect, createRef } from "react";
import {
  Card,
  CardActions,
  CardActionArea,
  CardContent,
  CardMedia,
  Button,
  Typography,
} from "@material-ui/core";
import axios from "axios";

import useStyles from "./styles";
import { Link, useHistory } from "react-router-dom";

const NewsCard = ({
  alanBtnRef,
  language,
  article,
  activeArticle,
  i,
  newsArticles,
  setNewsArticles,
}) => {
  const classes = useStyles();
  // console.log(newsArticles);
  const [elRefs, setElRefs] = useState([]);

  const scrollToRef = (ref) => window.scroll(0, ref.current.offsetTop - 50);
  useEffect(() => {
    window.scroll(0, 0);

    setElRefs((refs) =>
      Array(20)
        .fill()
        .map((_, j) => refs[j] || createRef())
    );
  }, []);

  useEffect(() => {
    if (i === activeArticle && elRefs[activeArticle]) {
      scrollToRef(elRefs[activeArticle]);
    }
  }, [i, activeArticle, elRefs]);

  const history = useHistory();

  const handleDetailPage = () => {
    alanBtnRef &&
      alanBtnRef.btnInstance.callProjectApi(
        "setClientData",
        { summary: article.content },
        function (error, result) {
          // handle error and result here
          console.log("Raj:" + error);
        }
      );
    // console.log(newsArticles);
    history.push({
      pathname: `/${i}`,
      state: {
        article: article,
        newsArticles: newsArticles,
        language: language,
      },
    });
  };

  const substr = (summary) => {
    return summary.substring(0, 100) + "...";
  };

  return (
    <Card
      ref={elRefs[i]}
      className={activeArticle === i ? classes.activeCard : classes.card}
    >
      <CardActionArea>
        <CardMedia
          className={classes.media}
          image={
            article.media ||
            "https://www.industry.gov.au/sites/default/files/August%202018/image/news-placeholder-738.png"
          }
          title={article.title}
        />
        <div className={classes.details}>
          <Typography variant="body2" color="textSecondary" component="h2">
            {new Date(article.published_date).toDateString()}
          </Typography>
          {/* <Typography variant="body2" color="textSecondary" component="h2">
            {source.name}
          </Typography> */}
        </div>
        <div style={{ height: "300px" }}>
          <Typography
            className={classes.title}
            gutterBottom
            variant="h5"
            component="h3"
          >
            {article.title}
          </Typography>
          <CardContent>
            <Typography variant="h6" color="textSecondary" component="h4">
              {substr(article.content)}
            </Typography>
          </CardContent>
        </div>
      </CardActionArea>
      <CardActions className={classes.cardActions}>
        {console.log()}
        <Button color="primary" onClick={handleDetailPage}>
          {console.log("language" + language)}
          {language == "English" ? (
            <>Learn More</>
          ) : language == "Hindi" ? (
            <>और अधिक जानें</>
          ) : (
            <>વધુ શીખો</>
          )}
        </Button>
        {/* <Button size="small" color="primary" href={url}>
          Learn More
        </Button> */}
        <Typography variant="h5" color="textSecondary" component="h2">
          {i + 1}
        </Typography>
      </CardActions>
    </Card>
  );
};

// The Indian Express
// Hindustan Times
// NDTV
// THE TOI
// Sportskeeda
// India Today
// India Forums
export default NewsCard;
