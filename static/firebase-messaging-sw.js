importScripts("https://www.gstatic.com/firebasejs/8.5.0/firebase-app.js")
importScripts("https://www.gstatic.com/firebasejs/8.5.0/firebase-messaging.js")

var config = {
    apiKey: "AIzaSyD3GChDdJ-GWTQsU1-rOYQbQcTIBbIAv78",
    authDomain: "covidmx-b6a28.firebaseapp.com",
    projectId: "covidmx-b6a28",
    storageBucket: "covidmx-b6a28.appspot.com",
    messagingSenderId: "547859078864",
    appId: "1:547859078864:web:96dc4763c20500f18648d5",
    measurementId: "G-YYCL4DP2BB"
  };

firebase.initializeApp(config);

const message = firebase.messaging();

message.setBackgroundMessageHandler((payload) => {
    const title = payload.notification.title;
    const options = {
        body: payload.notification.body
    }
    return self.ServiceWorkerRegistration.showNotification(title, options)
});