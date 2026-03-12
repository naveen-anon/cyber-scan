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
.then(data=>{
document.getElementById("results").innerHTML=
JSON.stringify(data,null,2)
})

}
