console.log("mohit");


  let a =[
      ["MOHIT","TALIB","AMAN","AJEET"],
      [20,20,23,24],
      ["BSC","B.C.A","B.COM","LLB"],
      ["GREATER","BIHAR","HALDONI","AGRA"]
  
];
  
document.write(a.length + "<br>");

document.write("<table style='border:1px dotted red'>")

for(let b=0; b < 4; b++){

    document.write("<tr>")

         for( let c= 0; c < 4; c++){

            document.write("<td>" + a[b][c]+ "</td>");
         }

         document.write("</tr>")

         

     document.write( "");
}

document.write("</table>")