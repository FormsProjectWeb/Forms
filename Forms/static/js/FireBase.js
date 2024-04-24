import {initializeApp} from "https://www.gstatic.com/firebasejs/9.8.4/firebase-app.js";
import {getFirestore, collection, onSnapshot, doc, setDoc, getDocs, getDoc, deleteDoc} from "https://www.gstatic.com/firebasejs/9.8.4/firebase-firestore.js";
import {getStorage, ref, uploadBytesResumable, getDownloadURL, deleteObject, listAll} from "https://www.gstatic.com/firebasejs/9.8.4/firebase-storage.js";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
    apiKey: "AIzaSyBDBWxGcDogsWYaUnQPkC7FVaoKRHsA78w",
    authDomain: "classes-85272.firebaseapp.com",
    projectId: "classes-85272",
    storageBucket: "classes-85272.appspot.com",
    messagingSenderId: "779324847488",
    appId: "1:779324847488:web:a391da7753b1a98e913d65",
    measurementId: "G-988FPZME9J"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const database = getFirestore();
const storage = getStorage(app);

export const putDatum = (section, id, datum)=>setDoc(doc(database, section, id), datum);
export const getData = (section)=>getDocs(collection(database, section));
export const getDataLive = (section, callBack)=>onSnapshot(collection(database, section), callBack);
export const getDatum = (section, id)=>getDoc(doc(database, section, id));
export const getDatumLive = (section, id, callBack)=>onSnapshot(doc(database, section, id), callBack);
export const removeDatum = (section, id)=>deleteDoc(doc(database, section, id));
export const putFile = (route, file, progressCallback)=>new Promise((resolve, reject)=>{uploadBytesResumable(ref(storage, route), file).on("state_changed", (snapshot)=>{if (progressCallback){progressCallback(snapshot.bytesTransferred, snapshot.totalBytes);}}, ()=>{reject()}, ()=>{resolve()});});
export const getFiles = (route)=>listAll(ref(storage, route));
export const getFile = (route)=>getDownloadURL(ref(storage, route));
export const removeFile = (route)=>deleteObject(ref(storage, route));