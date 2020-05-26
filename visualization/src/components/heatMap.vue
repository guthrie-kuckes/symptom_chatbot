<template>
  <GmapMap
    ref="heatmap"
    id="map"
    :center="{lat: this.lat, lng: this.lng}"
    :zoom="7"
    map-type-id="terrain"
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
    },
    mapStyle() {
      return [
        {
          elementType: "geometry",
          stylers: [
            {
              color: "#1d2c4d"
            }
          ]
        },
        {
          elementType: "labels.text.fill",
          stylers: [
            {
              color: "#8ec3b9"
            }
          ]
        },
        {
          elementType: "labels.text.stroke",
          stylers: [
            {
              color: "#1a3646"
            }
          ]
        },
        {
          featureType: "administrative",
          elementType: "geometry",
          stylers: [
            {
              visibility: "off"
            }
          ]
        },
        {
          featureType: "administrative.country",
          elementType: "geometry.stroke",
          stylers: [
            {
              color: "#4b6878"
            }
          ]
        },
        {
          featureType: "administrative.land_parcel",
          elementType: "labels.text.fill",
          stylers: [
            {
              color: "#64779e"
            }
          ]
        },
        {
          featureType: "administrative.province",
          elementType: "geometry.stroke",
          stylers: [
            {
              color: "#4b6878"
            }
          ]
        },
        {
          featureType: "landscape.man_made",
          elementType: "geometry.stroke",
          stylers: [
            {
              color: "#334e87"
            }
          ]
        },
        {
          featureType: "landscape.natural",
          elementType: "geometry",
          stylers: [
            {
              color: "#023e58"
            }
          ]
        },
        {
          featureType: "poi",
          stylers: [
            {
              visibility: "off"
            }
          ]
        },
        {
          featureType: "poi",
          elementType: "geometry",
          stylers: [
            {
              color: "#283d6a"
            }
          ]
        },
        {
          featureType: "poi",
          elementType: "labels.text.fill",
          stylers: [
            {
              color: "#6f9ba5"
            }
          ]
        },
        {
          featureType: "poi",
          elementType: "labels.text.stroke",
          stylers: [
            {
              color: "#1d2c4d"
            }
          ]
        },
        {
          featureType: "poi.park",
          elementType: "geometry.fill",
          stylers: [
            {
              color: "#023e58"
            }
          ]
        },
        {
          featureType: "poi.park",
          elementType: "labels.text.fill",
          stylers: [
            {
              color: "#3C7680"
            }
          ]
        },
        {
          featureType: "road",
          stylers: [
            {
              visibility: "off"
            }
          ]
        },
        {
          featureType: "road",
          elementType: "geometry",
          stylers: [
            {
              color: "#304a7d"
            }
          ]
        },
        {
          featureType: "road",
          elementType: "labels.icon",
          stylers: [
            {
              visibility: "off"
            }
          ]
        },
        {
          featureType: "road",
          elementType: "labels.text.fill",
          stylers: [
            {
              color: "#98a5be"
            }
          ]
        },
        {
          featureType: "road",
          elementType: "labels.text.stroke",
          stylers: [
            {
              color: "#1d2c4d"
            }
          ]
        },
        {
          featureType: "road.highway",
          elementType: "geometry",
          stylers: [
            {
              color: "#2c6675"
            }
          ]
        },
        {
          featureType: "road.highway",
          elementType: "geometry.stroke",
          stylers: [
            {
              color: "#255763"
            }
          ]
        },
        {
          featureType: "road.highway",
          elementType: "labels.text.fill",
          stylers: [
            {
              color: "#b0d5ce"
            }
          ]
        },
        {
          featureType: "road.highway",
          elementType: "labels.text.stroke",
          stylers: [
            {
              color: "#023e58"
            }
          ]
        },
        {
          featureType: "transit",
          stylers: [
            {
              visibility: "off"
            }
          ]
        },
        {
          featureType: "transit",
          elementType: "labels.text.fill",
          stylers: [
            {
              color: "#98a5be"
            }
          ]
        },
        {
          featureType: "transit",
          elementType: "labels.text.stroke",
          stylers: [
            {
              color: "#1d2c4d"
            }
          ]
        },
        {
          featureType: "transit.line",
          elementType: "geometry.fill",
          stylers: [
            {
              color: "#283d6a"
            }
          ]
        },
        {
          featureType: "transit.station",
          elementType: "geometry",
          stylers: [
            {
              color: "#3a4762"
            }
          ]
        },
        {
          featureType: "water",
          elementType: "geometry",
          stylers: [
            {
              color: "#0e1626"
            }
          ]
        },
        {
          featureType: "water",
          elementType: "labels.text.fill",
          stylers: [
            {
              color: "#4e6d70"
            }
          ]
        }
      ];
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
      var styledMap = new this.google.maps.StyledMapType(this.mapStyle, {
        name: "Styled Map"
      });
      console.log(styledMap);
        map.mapTypes.set('styled_map', styledMap);
        map.setMapTypeId('styled_map');
    });
  }
};
</script>