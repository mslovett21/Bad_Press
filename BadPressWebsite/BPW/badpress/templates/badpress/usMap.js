var width = 1440,
    height = 600;
    
    var svg = d3.select('body').append('svg')
    .attr('width', width)
    .attr('height', height);
        
    var projection = d3.geo.albersUsa()
    .scale(1000) 
    .translate([width / 2, height / 2]);
    
    var path = d3.geo.path()
    .projection(projection);
    
    d3.json('us.json', function(error, us) {
    svg.selectAll('.states')
    .data(topojson.feature(us, us.objects.usStates).features)
    .enter()
    .append("a")
    .attr("xlink:href", function(d) {return 'https://wikipedia.org/wiki/' + d.properties.STATE_ABBR})
    .append('path')
    .attr('class', 'states')
    .attr('d', path)
    .style("fill", function(d) {
    return d.properties.COLOR
    });
    });