    d3.csv("billboard_FINAL.csv").then(function(data) {
        // Data processing and chart creation will go here
        const width = 800;
        const height = 400;
        const margin = { top: 30, right: 30, bottom: 40, left: 50 };
    
        const svg = d3.select("#canvas")
          .attr("width", width)
          .attr("height", height);
    
        const chartArea = svg.append("g")
          .attr("transform", `translate(${margin.left},${margin.top})`);
    
        const chartWidth = width - margin.left - margin.right;
        const chartHeight = height - margin.top - margin.bottom;

        const x = d3
        .scaleBand()
        .domain(data.map(d => d.country))
        .range([0, chartWidth])
        .padding(0.1);

        const y = d3.scaleLinear()
        .domain([0, d3.max(data, d => +d.count)])
        .range([chartHeight, 0]);


        chartArea.selectAll(".bar")
      .data(data)
      .enter().append("rect")
        .attr("class", "bar")
        .attr("x", d => x(d.country))
        .attr("y", d => y(+d.count))
        .attr("width", x.bandwidth())
        .attr("height", d => chartHeight - y(+d.count))
        .attr("fill", "lightblue")
        .on("click", function(event, d) { // Add click event listener
          svg.select("#clicked-value") // Select the text element
            .text(`${d.count} artists are from ${d.country}.`); // Update the text with clicked bar's value
        });

        // Create text element for dynamic display
        svg.append("text")
        .attr("id", "clicked-value")
        .attr("x", 300)
        .attr("y", 50)
        .attr("text-anchor", "middle")
        .text(""); // Initially empty

        const xAxis = d3.axisBottom(x);
        const yAxis = d3.axisLeft(y);

        svg.append("text")
    .attr("class", "x label")
    .attr("text-anchor", "end")
    .attr("x", width)
    .attr("y", height)
    .attr("align", "center")
    .text("country of origin");

    svg.append("text")
    .attr("class", "y label")
    .attr("text-anchor", "end")
    .attr("y", -2)
    .attr("dy", ".80em")
    .attr("transform", "rotate(-90)")
    .text("# of artists");

        chartArea.append("g")
        .attr("transform", `translate(0, ${chartHeight})`)
        .call(xAxis);
  
      chartArea.append("g")
        .call(yAxis);
      });