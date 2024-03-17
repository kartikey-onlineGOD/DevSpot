// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
    apiKey: "AIzaSyD65a6WdCM5t_udjf0ibw1NqBF7WxF_0rs",
    authDomain: "hackpsu-2024-spring.firebaseapp.com",
    projectId: "hackpsu-2024-spring",
    storageBucket: "hackpsu-2024-spring.appspot.com",
    messagingSenderId: "332445091492",
    appId: "1:332445091492:web:e690240a97d90153bd8831",
    measurementId: "G-JXQY3YPCQS"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);