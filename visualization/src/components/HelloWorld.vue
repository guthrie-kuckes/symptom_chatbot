<template>
  <div>
    <vue-google-heatmap :points="points"
                      :width="400"
                      :height="350" 
             
                   
                      />
  </div>
</template>

<script>
 // Template zebras use

export default {
  name: 'HelloWorld',
  props: {
    msg: String
  },
  data() {
    return {
      points: [
        {lat: 37.786117, lng:-122.330119},
        {lat: 37.786117, lng:-122.330119},
        {lat: 37.786117, lng:-122.330119},
        {lat: 37.786117, lng:-122.340119},
        {lat: 37.786117, lng:-122.340119},
        {lat: 37.786117, lng:-122.440119},
        {lat: 37.786117, lng:-122.440119},
        {lat: 37.786117, lng:-122.440119},
        {lat: 37.786117, lng:-122.440119},
        {lat: 37.786117, lng:-122.440119},
        {lat: 37.786564, lng:-122.440209},
        {lat: 37.786905, lng:-122.440270},
        {lat: 37.786956, lng:-122.440279},
        {lat: 37.800224, lng:-122.433520},
        {lat: 37.800155, lng:-122.434101},
        {lat: 37.800160, lng:-122.434430},
        {lat: 37.800378, lng:-122.434527},
        {lat: 37.800738, lng:-122.434598},
        {lat: 37.800938, lng:-122.434650},
        {lat: 37.801024, lng:-122.434889},
        {lat: 37.800955, lng:-122.435392},
        {lat: 37.800886, lng:-122.435959}
      ]
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
