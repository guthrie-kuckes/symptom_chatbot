<template>
<v-layout align-center justify-center>
    <vue-google-heatmap :points="points"
                      width="100%"
                      height="100%"
                      :lat="42.3584300"
                      :lng="-71.0597700"
                      map-type="roadmap"
                   
                      />
</v-layout>
</template>

<script>
 // Template zebras use

export default {
  name: 'Map',
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
