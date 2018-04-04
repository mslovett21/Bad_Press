//replace with json
        var data = [
          {"name": "Gun Control ",
            "value": 80,
            },
          {"name": "Education ",
            "value": 66,
            },
          {"name": "Health Care ",
            "value": 72,
            },
          {"name": "Immigration ",
            "value": 28,
            },
          { "name": "Environment ",
            "value": 55,
            }
        ];

        //change to try out different margins
        var margin = {
            top: 20,
            right: 20,
            bottom: 20,
            left: 100 //padding left for data names
        };

        //size of bars
        var width = 460 - margin.left - margin.right,
            height = 350 - margin.top - margin.bottom;

        var svg = d3.select("#keyIssues").append("svg")
            .attr("width", width + margin.left + margin.right)
            .attr("height", height + margin.top + margin.bottom)
            .append("g")
            .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

        var x = d3.scale.linear()
            .range([0, width])
            .domain([0, d3.max(data, function (d) {
                return d.value;
            })]);

        var y = d3.scale.ordinal()
            .rangeRoundBands([height, 0], .1)
            .domain(data.map(function (d) {
                return d.name;
            }));

        //make y axis to show bar names
        var yAxis = d3.svg.axis()
            .scale(y)
            //no tick marks
            .tickSize(0)
            .orient("left");

        var gy = svg.append("g")
            .attr("class", "y axis")
            .call(yAxis)

        var bars = svg.selectAll(".bar")
            .data(data)
            .enter()
            .append("g")

        //append rects
        bars.append("rect")
            .attr("class", "bar")
            .attr("y", function (d) {
                return y(d.name);
            })
            .attr("height", y.rangeBand())
            .attr("x", 0)
            .attr("width", function (d) {
                return x(d.value);
            });