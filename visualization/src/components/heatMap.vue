<template>
  <GmapMap
    ref="heatmap"
    id="map"
    :center="{lat: this.lat, lng: this.lng}"
    :zoom="7"
    map-type-id="terrain"
    style="width: 500px; height: 300px"
  ></GmapMap>
</template>

<script>
import { gmapApi } from "vue2-google-maps";

export default {
  name: "heatmap",
  props: {
    lat: {
      type: Number,
      default: () => 37.775
    },
    lng: {
      type: Number,
      default: () => -122.434
    },
    initialZoom: {
      type: Number,
      default: () => 500
    },
    mapType: {
      type: String,
      default: () => "roadmap"
    },
    points: {
      type: Array,
      required: true
    },
    width: {
      type: [String, Number],
      default: () => "100%"
    },
    height: {
      type: [String, Number],
      default: () => "100%"
    },
    opacity: {
      type: Number,
      default: () => 1
    },
    maxIntensity: {
      type: Number,
      default: () => 5
    }
  },
  computed: {
    google: gmapApi,
    mapWidth() {
      if (typeof this.width === "string") {
        return this.width;
      } else {
        return `${this.width}px`;
      }
    },
    mapHeight() {
      if (typeof this.height === "string") {
        return this.height;
      } else {
        return `${this.height}px`;
      }
    },
    heatmapPoints() {
      return this.points.map(
        // eslint-disable-next-line
        point => new google.maps.LatLng(point.lat, point.lng)
      );
    }
  },
  mounted() {
    this.$gmapApiPromiseLazy().then(() => {
      var sanFrancisco = new this.google.maps.LatLng(this.lat, this.lng);
      var map = new this.google.maps.Map(document.getElementById("map"), {
        center: sanFrancisco,
        zoom: 13,
        mapTypeId: "terrain"
      });
      var heatmap = new this.google.maps.visualization.HeatmapLayer({
        data: this.heatmapPoints
      });
      heatmap.setMap(map);
    });
  }
};
</script>