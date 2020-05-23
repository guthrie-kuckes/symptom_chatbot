import firebase from "firebase/app";
import "firebase/auth"
import "firebase/firestore";

var firebaseConfig = {
    apiKey: "AIzaSyBoPENiji-slQ3gjdjEY1WRKOfNgatSpMU",
    authDomain: "symptom-chatbot.firebaseapp.com",
    databaseURL: "https://symptom-chatbot.firebaseio.com",
    projectId: "symptom-chatbot",
    storageBucket: "symptom-chatbot.appspot.com",
    messagingSenderId: "631219149444",
    appId: "1:631219149444:web:a52060cf60445e122380d1",
    measurementId: "G-M1BCXH3QKV"
};
// Initialize Firebase
const app = firebase.initializeApp(config);
const auth = firebase.auth();
const db = app.firestore();

export default app;
export { auth, db, authUI, authUIConfig };