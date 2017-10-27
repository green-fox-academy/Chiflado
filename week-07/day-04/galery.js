
let imagesData = [{'source':'url(https://scontent-vie1-1.xx.fbcdn.net/v/t1.0-9/13043558_10206566541949981_6049452993740991625_n.jpg?oh=28599ff39b4c32dc83ad2c854c5cc4e4&oe=5A7C420E)'},
              {'source':'url(https://scontent-vie1-1.xx.fbcdn.net/v/t1.0-9/10882297_10203753785832836_477210657233972734_n.jpg?oh=c5a25fe6fcae083b373c93117bd82539&oe=5A645C68)'},
              {'source':'url(https://scontent-vie1-1.xx.fbcdn.net/v/t1.0-9/10858537_10203435010343648_9020277979094162743_n.jpg?oh=50bf92040ba1809798aa72b7d52a412d&oe=5A62B9AA)'},
              {'source':'url(https://scontent-vie1-1.xx.fbcdn.net/v/t1.0-9/68105_10200991513537755_183500230_n.jpg?oh=7627d52ab1f6f1b928dfa7920e0a81e3&oe=5AA99C8E)'},
              {'source':'url(https://scontent-vie1-1.xx.fbcdn.net/v/t1.0-9/425424_2646955380839_1838109620_n.jpg?oh=60808b27409037dea9f1a6a13ecf5f41&oe=5AABF778)'},
              {'source':'url(https://scontent-vie1-1.xx.fbcdn.net/v/t1.0-9/17191004_10208960931728229_7862075380728748991_n.jpg?oh=12babb14a12b8eedf393960b1a11b305&oe=5A68189D)'},
              {'source':'url(https://scontent-vie1-1.xx.fbcdn.net/v/t1.0-9/16708563_10208759865581701_6572146831846316615_n.jpg?oh=3313254917edf9124413b71ff8eb35ee&oe=5A78CD5B)'},
              {'source':'url(https://scontent-vie1-1.xx.fbcdn.net/v/t1.0-9/14068089_10207397561004938_994714148296913399_n.jpg?oh=ace5ed933803ea1b64aaf83c70f1f91a&oe=5AAF08BD)'}
]

let images = document.querySelectorAll('.image');

function setThumbNails(){
    for (let i in images){
        images[i].style.background = (imagesData[i]['source']);
        images[i].style.backgroundSize = '200%';    
    }
};

setThumbNails();