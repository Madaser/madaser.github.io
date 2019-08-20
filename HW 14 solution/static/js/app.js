// from data.js

var text= d3.select(".form-control");
var button= d3.select("#filter-btn");
var tbody= d3.select("tbody");


    function handleChange(event) {
    
    var inputText = d3.event.target.value;
  
    var tableData = data;
    console.log(tableData)
    console.log(inputText);
    

    tableData.forEach(function(highsightings) {
       console.log(highsightings);
       
       if(highsightings["datetime"] === inputText) {
        var row=tbody.append("tr");

        Object.entries(highsightings).forEach(function([key, value]) {
         console.log(key, value);
         var cell=row.append("td");
         cell.text(value);
        });

       }

       else {
       }


    });



    
    }
text.on("change", handleChange);


