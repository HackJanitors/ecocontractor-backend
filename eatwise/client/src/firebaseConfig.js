// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyDcIo6Q5u9JCTWvzX5HXSH-7o_WVHx_oDo",
  authDomain: "eatwise-e531f.firebaseapp.com",
  projectId: "eatwise-e531f",
  storageBucket: "eatwise-e531f.appspot.com",
  messagingSenderId: "378959054118",
  appId: "1:378959054118:web:58cc7f9284cc139b566de7",
  measurementId: "G-13N5T4JZS3"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);