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

const messaging = firebase.messaging();

messaging.requestPermission()
.then(function (){
    console.log("Have Permissions");
    return messaging.getToken();
})
.then(function(token){
    console.log(token);
})
.catch(function(err){
    console.log("Error Ocurred: " + err);
});

messaging.onMessage((payload) => {
    const title = payload.notification.title;
    const body = payload.notification.body;

    var noti = "<div class=\"toast\" style=\"min-width: 300px;\" role=\"alert\" aria-live=\"assertive\" aria-atomic=\"true\" data-autohide=\"false\">"+
                    "<div class=\"toast-header\">"+
                        "<img src=\"assets/img/apple-touch-icon-3.png\" class=\"rounded mr-2\" width=\"24\" height=\"24\">"+
                        "<strong class=\"mr-auto\">"+ title +"</strong>"+
                        "<small class=\"text-muted\">Ahora mismo</small>"+

                        "<button type=\"button\" class=\"ml-2 mb-1 close\" data-dismiss=\"toast\" aria-label=\"Close\" onClick=\"deleteNoti(this)\">"+
                            "<span aria-hidden=\"true\">&times;</span>"+
                        "</button>"+
                    "</div>"+
                    "<div class=\"toast-body\">"+
                        body +
                    "</div>"+
                "</div>";

    console.log('Message received. ', payload);
    
    $("#notifications").append(noti);
    $('.toast').toast('show');
    const audio = new Audio('notification.mp3');
    audio.play();
  });

  function deleteNoti(element){
    var noti = $(element).parents(".toast")[0];
    noti.remove();
  }