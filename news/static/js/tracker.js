// ================== find if news article is in viewport =================
var news = document.getElementById("news");

prevElemTop = news.getBoundingClientRect().top;
prevElemBottom = news.getBoundingClientRect().bottom;

function newsArticleIsInViewport() {
  elemTop = news.getBoundingClientRect().top;
  elemBottom = news.getBoundingClientRect().bottom;
  if (elemTop > window.innerHeight || elemBottom < 0) {
    return false;
  } else {
    return true;
  }
}
// ========================= init newsArticleWasInViewport =======
var prevTimestamp = new Date(Date.now());
var newsArticleWasInViewport = false;
if (newsArticleIsInViewport()) {
  newsArticleWasInViewport = true;
} else {
  newsArticleWasInViewport = false;
}
console.log("newsArticleIsInViewport = " + newsArticleWasInViewport);

// ========================== scroll track ========================
var readTimeInSecs = 0;
window.addEventListener("scroll", function() {
  var currentTimestamp = new Date(Date.now());
  timeDiffInMillis = currentTimestamp - prevTimestamp;
  timeDiffInSecs = timeDiffInMillis / 1000;
  prevTimestamp = currentTimestamp;
  // console.log("Difference = " + timeDiffInSecs);
  if (newsArticleWasInViewport) {
    if (newsArticleIsInViewport()) {
      readTimeInSecs += timeDiffInSecs;
      newsArticleWasInViewport = true;
    } else {
      //send data
      readTimeInSecs = Math.floor(readTimeInSecs * 100) / 100;
      // alert("readTimeInSecs = " + readTimeInSecs);
      sendData(readTimeInSecs);
      console.log(">>>readTimeInSecs = " + readTimeInSecs);
      console.log("Data Sent");
      newsArticleWasInViewport = false;
    }
  } else {
    // div.innerHTML = "ID=" + newsId + " | " + new Date(Date.now()).toUTCString();
    readTimeInSecs = 0;
    if (newsArticleIsInViewport()) {
      newsArticleWasInViewport = true;
    } else {
      newsArticleWasInViewport = false;
    }
  }
});

// ================== cookie =================
//6.04e+8 --> a week in milliseconds
function createCookie(clientID) {
  var now = new Date();
  var year = now.getUTCFullYear();
  var expireYear = year + 10;
  now.setYear(expireYear);
  document.cookie =
    "clientId=" + clientID + ";expires=" + now.toUTCString() + ";path=/";
  console.log("cookie -> " + document.cookie);
}

function getCookie(name) {
  var value = "; " + document.cookie;
  var parts = value.split("; " + name + "=");
  if (parts.length == 2)
    return parts
      .pop()
      .split(";")
      .shift();
}

function updateExpirationDate(clientId) {
  var now = new Date();
  var year = now.getUTCFullYear();
  var expireYear = year + 10;
  now.setYear(expireYear);
  document.cookie =
    "clientId=" + clientId + ";expires=" + now.toUTCString() + ";path=/";
}

// ================= check cookie ==================
if (document.cookie.indexOf("clientId") >= 0) {
  console.log("Client ID found ... expiration updated");
  updateExpirationDate(getCookie("clientId"));
  console.log(getCookie("clientId"));
} else {
  console.log("Client ID not found ... hence created");
  // createCookie();
  //ajax call for user id and create clientId  cookie
  $.ajax({
    url: "http://127.0.0.1:8000/drf/random-id/",
    contentType: 'application/json',
    dataType: 'json',
    success: function (result) {
        console.log("Success >>> " + JSON.stringify(result));
        createCookie(result.userID);
    }, error: function () {
      console.log("ERROR ");
    }
});
}

// ================= csrf token ==============
function getCookie(name) {
  var cookieValue = null;
  if (document.cookie && document.cookie !== '') {
      var cookies = document.cookie.split(';');
      for (var i = 0; i < cookies.length; i++) {
          var cookie = cookies[i].trim();
          // Does this cookie string begin with the name we want?
          if (cookie.substring(0, name.length + 1) === (name + '=')) {
              cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
              break;
          }
      }
  }
  return cookieValue;
}
var csrftoken = getCookie('csrftoken');
console.log(csrftoken);

// ================= send data ===============
function sendData(readTimeInSecs) {
          // var params = {'userID': 12345,'newsID': newsId};
          
    $.ajax({
          url: "http://127.0.0.1:8000/drf/log-data/",
          method: "POST",
          // method: "POST",
          dataType: 'json',
          // contentType: 'application/json',
          // contentType: false,
          data: {'userID': getCookie("clientId"),'newsID': newsId},
          // data: form,
          // headers : {"X-CSRFToken": csrftoken}
          // "processData": false,
          // "mimeType": "multipart/form-data",
          // success: function (data) {
          //     alert("Success" + data);
          // }, error: function (data) {
          //   alert("ERROR >> "+data);
          // }
    });
}

// =================== single news tag fix =============
var singleNewsContent = document.getElementById("single-news-content");
var convert = function(convert) {
  return $("<span />", { html: convert }).text();
};
singleNewsContent.innerHTML = convert(singleNewsContent.innerHTML);

// =================== remove feature tag from single news ===================
var figureArray = singleNewsContent.getElementsByTagName("figure");
// console.log(figureArray);
$.each(figureArray, function(i, el) {
  // console.log(el);
  el.style.display = "none";
});