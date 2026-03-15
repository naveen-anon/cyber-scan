function usernameSearch(){

let username=document.getElementById("username").value

let html=`

<a href="https://github.com/${username}" target="_blank">GitHub</a><br>
<a href="https://twitter.com/${username}" target="_blank">Twitter</a><br>
<a href="https://instagram.com/${username}" target="_blank">Instagram</a><br>
<a href="https://www.google.com/search?q=${username}" target="_blank">Google Search</a>

`

document.getElementById("username_result").innerHTML=html

}


async function shodanLookup(){

let ip=document.getElementById("ip").value

let res=await fetch(`https://api.shodan.io/shodan/host/${ip}?key=YOUR_API_KEY`)

let data=await res.json()

document.getElementById("shodan_result").innerText=JSON.stringify(data,null,2)

}


function domainLookup(){

let domain=document.getElementById("domain").value

let url=`https://api.hackertarget.com/whois/?q=${domain}`

document.getElementById("domain_result").innerHTML=

`<a href="${url}" target="_blank">View WHOIS Data</a>`

}
