am5.ready(function() {
    // Create root element
    // https://www.amcharts.com/docs/v5/getting-started/#Root_element
    var root = am5.Root.new("chartdiv");
    let ytdBefore = document.getElementById("ytd_net_income").value;

    let ytdBeforeInt = dollarsToNum(ytdBefore);

    function dollarsToNum(str) {
        let sign = 1;
        if (str.includes("(")) {
            sign = -1;
        }

        let newStr = str.replace(/\$|,|\(|\)/g, "");

        return sign * parseInt(newStr);
    }
    function numToDollars(num) {
        if (num < 0) {
        }
    }

    // Set themes
    // https://www.amcharts.com/docs/v5/concepts/themes/
    root.setThemes([am5themes_Animated.new(root)]);

    // Create chart
    // https://www.amcharts.com/docs/v5/charts/xy-chart/
    var chart = root.container.children.push(
        am5xy.XYChart.new(root, {
            panX: false,
            panY: false,
            wheelX: "panX",
            wheelY: "zoomX",
            layout: root.verticalLayout,
        })
    );

    // Data
    var data = [
        {
            netIncome: "Net Income\nBefore and After\nDepreciation",
            before: ytdBeforeInt,
            after: 802645,
        },
    ];

    // Create axes
    // https://www.amcharts.com/docs/v5/charts/xy-chart/axes/
    var yAxis = chart.yAxes.push(
        am5xy.CategoryAxis.new(root, {
            categoryField: "netIncome",
            renderer: am5xy.AxisRendererY.new(root, {
                inversed: true,
                cellStartLocation: 0.1,
                cellEndLocation: 0.9,
            }),
        })
    );

    yAxis.data.setAll(data);

    var xAxis = chart.xAxes.push(
        am5xy.ValueAxis.new(root, {
            renderer: am5xy.AxisRendererX.new(root, {
                strokeOpacity: 0.1,
            }),
            min: 0,
        })
    );

    // Add series
    // https://www.amcharts.com/docs/v5/charts/xy-chart/series/
    function createSeries(field, name) {
        var series = chart.series.push(
            am5xy.ColumnSeries.new(root, {
                name: name,
                xAxis: xAxis,
                yAxis: yAxis,
                valueXField: field,
                categoryYField: "netIncome",
                sequencedInterpolation: true,
                tooltip: am5.Tooltip.new(root, {
                    pointerOrientation: "vertical",
                    labelText: "[bold]{name}[/]\n ({valueX})",
                }),
            })
        );

        series.columns.template.setAll({
            height: am5.p100,
            strokeOpacity: 0,
        });

        series.bullets.push(function() {
            return am5.Bullet.new(root, {
                locationX: 1,
                locationY: 0.5,
                sprite: am5.Label.new(root, {
                    centerY: am5.p50,
                    text: "({valueX})",
                    populateText: true,
                    // adapter: {
                    //     text: function(text, target) {
                    //         // Modify the label text based on the value (valueX)
                    //         const valueX = target.dataItem.get("valueX");
                    //         if (valueX < 0) {
                    //         }
                    //         return "(" + valueX + ")";
                    //     },
                    // },
                }),
            });
        });

        series.bullets.push(function() {
            return am5.Bullet.new(root, {
                locationX: 1,
                locationY: 0.5,
                sprite: am5.Label.new(root, {
                    centerX: am5.p100,
                    centerY: am5.p50,
                    text: "{name}",
                    fill: am5.color(0xffffff),
                    populateText: true,
                }),
            });
        });

        series.data.setAll(data);
        series.appear();

        return series;
    }

    createSeries("before", "Before");
    createSeries("after", "After");

    // Add legend
    // https://www.amcharts.com/docs/v5/charts/xy-chart/legend-xy-series/
    // var legend = chart.children.push(am5.Legend.new(root, {
    //   centerX: am5.p50,
    //   x: am5.p50
    // }));
    //
    // legend.data.setAll(chart.series.values);

    // Add cursor
    // https://www.amcharts.com/docs/v5/charts/xy-chart/cursor/
    var cursor = chart.set(
        "cursor",
        am5xy.XYCursor.new(root, {
            behavior: "zoomY",
        })
    );
    cursor.lineY.set("forceHidden", true);
    cursor.lineX.set("forceHidden", true);

    // Make stuff animate on load
    // https://www.amcharts.com/docs/v5/concepts/animations/
    chart.appear(1000, 100);
}); // end am5.ready()
