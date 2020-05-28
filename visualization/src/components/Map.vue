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
  props: {
    points: Array
  }
}
</script>

<style scoped>
div{
  height: 100%;
  width: 100%;
}
</style>
