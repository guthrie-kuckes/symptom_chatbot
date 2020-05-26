<template>
<v-layout align-center justify-center>
    <heatmap :points="points"  :lat="points[0].lat" :lng="points[0].lng"/>
</v-layout>
</template>

<script>
 import heatmap from './heatMap';

export default {

  name: 'Map',
  components:{heatmap},
  data() {
    return {
      points: [
        {lat: 42.3584300, lng:-71.0597700},
        {lat: 42.357117, lng:-71.059719},
        {lat: 42.356117, lng:-71.059719},
        {lat: 42.354117, lng:-71.058719},
        {lat: 42.356117, lng:-71.059919},
        {lat: 42.356117, lng:-71.059019},
        {lat: 42.356117, lng:-71.059719},
      ]
    }
  }
}
</script>

<style scoped>
div{
  height: 100%;
  width: 100%;
}
</style>
