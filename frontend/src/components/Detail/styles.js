import { makeStyles } from "@material-ui/core/styles";

export default makeStyles((theme) => ({
  roots: {
    marginTop: "2rem",
    backgroundColor: theme.palette.background.paper,
    width: "100%",
  },
  category: {
    width: "100%",
    height: "200px",
    marginBottom: "30px",
  },
  wrapper: {
    width: "100%",
    height: "100%",
    padding: "20px",
  },
  details: {
    marginTop: "80px",
    display: "flex",
  },
  article: {
    flex: "2",
  },
  articleWrapper: {
    width: "100%",
    height: "100%",
    padding: "20px",
    display: "flex",
    flexDirection: "column",
    justifyContent: "center",
  },
  title: {
    fontWeight: "bold",
    fontSize: "32px",
  },
  recommendation: {
    flex: "1",
  },
  recWrapper: {
    width: "100%",
    height: "100%",
    padding: "20px",
  },

  footer: {
    textAlign: "center",
    position: "fixed",
    left: 0,
    bottom: 0,
    color: "black",
    width: "100%",
    display: "flex",
    alignItems: "center",
    justifyContent: "center",
    height: "120px",
    [theme.breakpoints.down("sm")]: {
      display: "none",
    },
  },
  link: {
    textDecoration: "none",
    color: "rgba(21, 101, 192)",
  },
  image: {
    height: "450px",
    width: "100%",
    borderRadius: "10px",
    objectFit: "cover",
  },
  card: {
    display: "flex",
    justifyContent: "center",
    alignItems: "center",
    width: "100%",
    borderRadius: 10,
    color: "white",
    textAlign: "center",
    height: "175px",
    [theme.breakpoints.down("md")]: {
      height: "200px",
    },
    [theme.breakpoints.down("sm")]: {
      flexDirection: "column-reverse",
      textAlign: "center",
      width: "100%",
      height: "225px",
    },
  },
  left: {
    width: "60%",
    [theme.breakpoints.down("sm")]: {
      width: "100%",
    },
  },
  right: {
    width: "30%",
    [theme.breakpoints.down("sm")]: {
      width: "100%",
    },
  },
  authorBox: {
    backgroundColor: "#333",
    color: "white",
    display: "flex",
    justifyContent: "space-between",
    alignItems: "center",
    width: "100%",
    borderRadius: "10px",
    padding: "10px 20px",
    marginBottom: "1rem",
    [theme.breakpoints.down("sm")]: {
      display: "block",
    },
  },
  box: {
    width: "96%",
    margin: "0 auto",
    [theme.breakpoints.down("sm")]: {
      width: "100%",
    },
  },
  infoContainer: {
    display: "flex",
    alignItems: "center",
    justifyContent: "space-around",
    [theme.breakpoints.down("sm")]: {
      flexDirection: "column",
    },
  },
  recCard: {
    display: "flex",
  },
  recCardOne: {
    flex: "2",
  },
  recCard: {
    flex: "1",
  },
  articleTitle: {
    fontSize: "30px",
    fontWeight: "thin",
  },
  logoContainer: {
    padding: "0 5%",
    display: "flex",
    justifyContent: "space-around",
    alignItems: "center",
    width: "100%",
    [theme.breakpoints.down("sm")]: {
      flexDirection: "column-reverse",
      textAlign: "center",
    },
  },
  alanLogo: {
    height: "27vmin",
    borderRadius: "15%",
    padding: "0 5%",
    margin: "3% 0",
    [theme.breakpoints.down("sm")]: {
      height: "35vmin",
    },
  },

  // recommendation
  imgs: {
    height: "260px",
  },
  root: {
    display: "flex",
    height: 200,
    borderRadius: "10px",
  },
  details: {
    height: "100%",
    width: "55%",
  },
  content: {
    // flex: '1 0 auto',
    padding: "5px 10px",
    height: "100%",
  },
  cover: {
    width: "45%",
    height: 200,
    objectFit: "cover",
  },

  flex_center: {
    display: "flex",
    justifyContent: "space-between",
    alignItems: "center",
  },
  author_box: {
    height: "633px",
    overflowY: "scroll",
  },
  recommend_img: {
    borderTopRight: "10px",
    borderTopleft: "10px",
  },
  recommendation_box: {
    height: "400px",
    borderRadius: "10px",
    width: "96%",
    margin: "0 auto",
    [theme.breakpoints.down("xs")]: {
      width: "100%",
    },
  },
  paper: {
    borderRadius: "10px",
  },
  recommendation: {
    marginTop: "1rem",
    [theme.breakpoints.down("xs")]: {
      marginBottom: "4rem",
    },
  },
  marginTop: {
    marginTop: "2rem",
  },
  marginBottom: {
    marginBottom: "3rem",
  },
  scrollBar: {
    "&::-webkit-scrollbar": {
      width: "0.4em",
    },
    "&::-webkit-scrollbar-track": {
      "-webkit-box-shadow": "inset 0 0 6px rgba(0,0,0,0.00)",
    },
    "&::-webkit-scrollbar-thumb": {
      backgroundColor: "rgba(0,0,0,.1)",
      borderRadius: "10px",
    },
  },
  dcard: {
    display: "flex",
    justifyContent: "center",
    alignItems: "center",
    width: "50%",
    padding: "3%",
    borderRadius: 10,
    color: "white",
    backgroundColor: "rgba(21, 101, 192)",
    margin: "0 12px",
    textAlign: "center",
    height: "25vmin",
    [theme.breakpoints.down("sm")]: {
      flexDirection: "column-reverse",
      textAlign: "center",
      width: "100%",
      height: "initial",
      "&:nth-of-type(1)": {
        marginBottom: "12px",
      },
    },
  },
  dinfoContainer: {
    display: "flex",
    alignItems: "center",
    justifyContent: "space-around",
    [theme.breakpoints.down("sm")]: {
      flexDirection: "column",
    },
  },
  dlogoContainer: {
    padding: "0 5%",
    display: "flex",
    justifyContent: "space-around",
    alignItems: "center",
    width: "100%",
    [theme.breakpoints.down("sm")]: {
      flexDirection: "column-reverse",
      textAlign: "center",
    },
  },
}));
