var data = []


var xa = [{% for item in values %}
            {{item}}, 
           {% endfor %}]
for(i=1;i<=24;i++)
{
   var map = {};
   map['id'] = i;
   map['x'] = xa[i-1] ;
   map['y'] = xa[i-1];
   data.push(map);
}            

var props = {
  data: data,
  width: 800,
  height: 400,
  initiated: true,
  x: function(d) {
    return d.id;
  },
  fieldY: [{
    name: "x",
    color: "#1f77b4",
    type: "LINE_CHART"
  },{
    name: "y",
    color: "#1f77b4",
    type: "AREA_CHART"
  }]
};

ReactDOM.render(React.createElement(LinkedMultipleChart, props), document.getElementById('chart'));