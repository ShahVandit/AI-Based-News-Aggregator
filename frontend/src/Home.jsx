import React, { useState, useEffect, useRef } from "react";
import { Typography, Backdrop, CircularProgress } from "@material-ui/core";
import wordsToNumbers from "words-to-numbers";
import alanBtn from "@alan-ai/alan-sdk-web";

import news from "./images/news.png";
import { NewsCards, Modal } from "./components";
import useStyles from "./styles";

import axios from "axios";
import Navbar from "./components/navbar/Navbar";

const Home = () => {
  const [dummy, setDummy] = useState(false);
  const [activeArticle, setActiveArticle] = useState(0);
  const [newsArticles, setNewsArticles] = useState([]);
  const [isOpen, setIsOpen] = useState(false);
  const [searchedArticles, setSearchedArticles] = useState([]);
  const [search, setSearch] = useState("");
  const [language, setLanguage] = useState("English");
  const [loading, setLoading] = useState(false);

  const NEWS_API_KEY = process.env.REACT_APP_CATCHER_KEY;

  const options = ["English", "Hindi", "Gujarati"];
  const onOptionChangeHandler = async (event) => {
    const cur_lang = language;
    setLanguage(event.target.value);
    localStorage.setItem("language", JSON.stringify(event.target.value));
    if (newsArticles?.length > 0) {
      setLoading(true);
      const response = await axios.post("http://127.0.0.1:8000/translate/", {
        articles: newsArticles,
        language: event.target.value,
        cur_lang: cur_lang,
      });
      setNewsArticles(response.data);
      setLoading(false);
      localStorage.setItem("articles", JSON.stringify(response.data));
    }
  };

  const classes = useStyles();

  // ALAN SIDE - intent(what does alan listen for)
  const alanBtnRef = useRef({}).current;
  useEffect(() => {
    if (language === "English") {
      console.log(language);
      alanBtnRef.btnInstance = alanBtn({
        key: process.env.REACT_APP_ALAN_KEY + "/stage",
        onCommand: async ({ command, articles, number, num }) => {
          if (command === "newHeadlines") {
            console.log(articles);
            articles = articles.slice(0, Math.min(20, articles.length));
            const res = await axios.post(`http://127.0.0.1:8000/scrape/`, {
              articles: articles,
            });
            articles = res.data;
            if (language !== "English" && articles?.length > 0) {
              const response = await axios.post(
                "http://127.0.0.1:8000/translate/",
                {
                  articles: articles,
                  language: language,
                  cur_lang: "English",
                }
              );
              setNewsArticles(response.data);
              if (articles?.length > 0) {
                localStorage.setItem("articles", JSON.stringify(response.data));
              } else localStorage.removeItem("articles");
            } else {
              setNewsArticles(articles);
              localStorage.setItem("articles", JSON.stringify(articles));
            }
            setActiveArticle(-1);
          } else if (command === "instructions") {
            setIsOpen(true);
          } else if (command === "active") {
            setActiveArticle(num - 2);
          } else if (command === "highlight") {
            setActiveArticle((prevActiveArticle) => prevActiveArticle + 1);
          } else if (command === "open") {
            const parsedNumber =
              number.length > 2
                ? wordsToNumbers(number, { fuzzy: true })
                : number;
            const article = articles[parsedNumber - 1];

            if (parsedNumber > articles?.length) {
              alanBtn().playText("Please try that again...");
            } else if (article) {
              window.open(article.url, "_blank");
              alanBtn().playText("Opening...");
            } else {
              alanBtn().playText("Please try that again...");
            }
          }
          // else if(command === 'stop'){
          //   console.log("stop");
          //   alanBtn().deactivate();
          // }
        },
      });
    }
  }, []);

  // search news
  const searchNews = async () => {
    if (search === "") return;
    setLoading(true);
    const response = await axios.get(
      `https://api.newscatcherapi.com/v2/search?countries=IN&lang=en&q=${search}`,
      {
        headers: { "x-api-key": NEWS_API_KEY },
      }
    );
    var data = response.data.articles.slice(
      0,
      Math.min(20, response.data.articles.length)
    );
    const res = await axios.post(`http://127.0.0.1:8000/scrape/`, {
      articles: data,
    });
    var sres = [];
    data = res.data;
    // const res = await axios.post(`http://127.0.0.1:8000/search/`, {
    //   searchText: search,
    // });
    // const data = res.data;
    if (language !== "English") {
      const responsee = await axios.post("http://127.0.0.1:8000/translate/", {
        articles: data,
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
      sres = data.sort(
        (a1, a2) => new Date(a2.date).getTime() - new Date(a1.date).getTime()
      );
      setNewsArticles(sres);
      setLoading(false);
      localStorage.setItem("articles", JSON.stringify(sres));
    }

    alanBtnRef.btnInstance.callProjectApi(
      "setArticles",
      { articles: sres },
      function (error, result) {
        // handle error and result here
        console.log("Raj:" + error);
      }
    );
  };

  useEffect(() => {
    const arti = JSON.parse(localStorage.getItem("articles"));
    const lang = JSON.parse(localStorage.getItem("language"));
    setLanguage(lang);
    if (arti?.length) {
      setNewsArticles(arti);
      console.log(arti);
      alanBtnRef.btnInstance.callProjectApi(
        "setArticles",
        { articles: arti },
        function (error, result) {
          // handle error and result here
          console.log("Raj:" + error);
        }
      );
    }
  }, []);
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
      <Navbar
        searchNews={searchNews}
        search={search}
        setSearch={setSearch}
        onOptionChangeHandler={onOptionChangeHandler}
        setLanguage={setLanguage}
        setNewsArticles={setNewsArticles}
        options={options}
        language={language}
      />
      <div>
        <div className={classes.logoContainer}>
          {newsArticles?.length ? (
            <div
              className={classes.infoContainer}
              style={{ marginTop: "2rem", marginBottom: "2rem" }}
            >
              {language === "English" && (
                <div className={classes.card}>
                  <Typography variant="h5" component="h2">
                    Try saying: <br />
                    <br />
                    Open article number [4]
                  </Typography>
                </div>
              )}
              {language === "English" && (
                <div className={classes.card}>
                  <Typography variant="h5" component="h2">
                    Try saying: <br />
                    <br />
                    Go back
                  </Typography>
                </div>
              )}
            </div>
          ) : null}
        </div>
        <NewsCards
          alanBtnRef={alanBtnRef}
          language={language}
          articles={newsArticles}
          activeArticle={activeArticle}
          newsArticles={newsArticles}
          setNewsArticles={setNewsArticles}
          setDummy={setDummy}
        />
        <Modal isOpen={isOpen} setIsOpen={setIsOpen} />
        {/* {!newsArticles.length ? (
        <div className={classes.footer}>
          <Typography variant="body1" component="h2">
            Created by
            <a
              className={classes.link}
              href="https://www.linkedin.com/in/adrian-hajdin/"
            >
              {" "}
              Adrian Hajdin
            </a>{" "}
            -
            <a
              className={classes.link}
              href="http://youtube.com/javascriptmastery"
            >
              {" "}
              JavaScript Mastery
            </a>
          </Typography>
          <img
            className={classes.image}
            src={logo}
            height="50px"
            alt="JSMastery logo"
          />
        </div>
      ) : null} */}
      </div>
    </>
  );
};

export default Home;
