document.write("<!DOCTYPE html><html lang='en'><head><script rel='../static/scripts/index.js'></script><link rel='stylesheet' href='.././static/style.css'><meta charset='UTF-8'><meta name='viewport' content='width=device-width, initial-scale=1.0'><link rel='preconnect' href='https://fonts.googleapis.com'><link rel='preconnect' href='https://fonts.gstatic.com' crossorigin><link href='https://fonts.googleapis.com/css2?family=Roboto:wght@300&display=swap' rel='stylesheet'></script><title>Terminal</title></Head><body><div class='header'><div class='nav'></div></div><div class='main'></div><div class='footer'><div class='footerTop'><div class='frameOne'><div></div><div id='pricing' class='askPrice'><p class='beforePoint'>100000.</p><p class='afterPoint'>0</p></div><div class='lots'><p>0.00</p><div></div></div><div id='pricing' class='askPrice'><p class='beforePoint'>100000.</p> <p class='afterPoint'>0</p></div><div></div></div><div class='frameTwo'><div class='footerButtons'><div id='button' class='buttonZero' onclick='sell();'><p>Sell</p></div><span></span><div id='button' class='buttonOne' onclick='buy()'><p>Buy</p></div></div></div><div class='frameThree'></div></div></div><div class='fotterBottom'></div></body></html>");

let request = {
    "sell": false,"buy": false,
};

function sell() {

    
    let option = {
        "sell": true,"buy": false
    };
    
    console.log(option);


    


};

function buy() {

    let option = {
        "sell": false,"buy": true,
    }

    console.log(option)

};