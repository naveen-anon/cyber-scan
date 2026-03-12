function show(data){

document.getElementById("results").textContent =
JSON.stringify(data,null,2)

}

function ipSearch(){

let ip=document.getElementById("ip").value

fetch("/ip_lookup",{
method:"POST",
headers:{
"Content-Type":"application/x-www-form-urlencoded"
},
body:"ip="+ip
})
.then(r=>r.json())
.then(show)

}

function usernameSearch(){

let u=document.getElementById("username").value

window.open("https://www.google.com/search?q="+u)

}

function phoneSearch(){

let p=document.getElementById("phone").value

window.open("https://www.google.com/search?q="+p)

}

function domainSearch(){

let d=document.getElementById("domain").value

window.open("https://who.is/whois/"+d)

}

function emailSearch(){

let e=document.getElementById("email").value

window.open("https://www.google.com/search?q="+e)

}
