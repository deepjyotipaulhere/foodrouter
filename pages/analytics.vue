<template>
  <div>
        <div class="ui container">
            <div class="ui segment">
                <div id="chartContainer" style="width: 100%;height:400px"></div>
            </div>
            <div class="ui segment">
                <h2>Advertising target</h2>
                <div class="ui info message">
                    <div class="header">
                        Residents in <b>3rd Cross Road, Indiranagar, Bangalore, Karnataka, 743123</b> may be targeted with products like <br>
                        <br>
                        <a class="ui tag teal label">Refrigerator</a>
                        <a class="ui tag teal label">Rice Cooker</a>
                        <a class="ui tag teal label">Rice Cooker</a>
                    </div>
                </div>
                <div class="ui warning message">
                    <div class="header">
                        Residents in <b>10 Ak Sarani, Indiranagar, Bangalore, Karnataka, 743128</b> may be targeted with products like <br>
                        <br>
                        <a class="ui tag orange label">Automatic Dosa Maker</a>
                        <a class="ui tag orange label">20% off for next 5 Swiggy orders</a>
                        <a class="ui tag orange label">Exclusive discount at a restaurant near you</a>
                    </div>
                </div>
            </div>
        </div>
  </div>
</template>

<script>
export default {
    data() {
        return {
            chartOptions: {
                title: {
                    text: "Zone-wise Wastage Report"
                },
                data: [
                    {
                    type: "column",
                    dataPoints: [
                        { label: '3rd Cross Road, Indiranagar, Bangalore, Karnataka, 743123', y: 71 },
                        { label: '4th Cross Road, Indiranagar, Bangalore, Karnataka, 743125', y: 30 },
                        { label: '10th Avenue, Indiranagar, Bangalore, Karnataka, 743128', y: 10 },
                        { label: '10th Avenue, Indiranagar, Bangalore, Karnataka, 743128', y: 8 },
                        { label: '91, springboard Road, Indiranagar, Bangalore, Karnataka, 743128', y: 9 },
                        { label: '10 A.J.C Bose Road, Indiranagar, Bangalore, Karnataka, 743128', y: 5 },
                        { label: '10 Ak Sarani, Indiranagar, Bangalore, Karnataka, 743128', y: 2 },
                    ]
                    }
                ],
                 axisX:{
                    labelAutoFit: true,
                    labelAngle: -45
                },
            },
            chart: null,
            locations:[]
        }
    },
    mounted: function() {
        this.chart = new CanvasJS.Chart("chartContainer", this.chartOptions);
        this.chart.render();
    },
};
</script>

<style>
</style>