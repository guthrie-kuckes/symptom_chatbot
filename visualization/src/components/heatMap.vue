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
// import {jsonString} from "../MA.js";

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
      default: () => 13
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
      console.log("Points used are: ", this.points[0]);
      return this.points.map(
        // eslint-disable-next-line
        point => new google.maps.LatLng(point.lat, point.lng)
      );
    },
    gradient(){
      return [
          'rgba(0, 255, 255, 0)',
          'rgba(0, 255, 255, 1)',
          'rgba(0, 191, 255, 1)',
          'rgba(0, 127, 255, 1)',
          'rgba(0, 63, 255, 1)',
          'rgba(0, 0, 255, 1)',
          'rgba(0, 0, 223, 1)',
          'rgba(0, 0, 191, 1)',
          'rgba(0, 0, 159, 1)',
          'rgba(0, 0, 127, 1)',
          'rgba(63, 0, 91, 1)',
          'rgba(127, 0, 63, 1)',
          'rgba(191, 0, 31, 1)',
          'rgba(255, 0, 0, 1)'
        ]
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
    },
    center() {
      return new this.google.maps.LatLng(this.lat, this.lng);
    },
    options() {
      return {
        center: this.center,
        zoom: this.initialZoom,
        mapTypeId: this.mapType,
        streetViewControl: false,
        mapTypeControl: false
      };
    },
    JSONurl(){
      return 'http://bostonopendata-boston.opendata.arcgis.com/datasets/53ea466a189b4f43b3dfb7b38fa7f3b6_1.geojson?outSR={%22latestWkid%22:2249,%22wkid%22:102686}';
    },
    JSONStyle(){
      return {fillOpacity: 0.0, strokeWeight: 1, strokeColor: 'white',strokeOpacity:0.1 };
    }

  },
  methods: {
    drawMap: function() {
      // Getting map
      this.$refs.heatmap.$mapPromise.then(map => {
        map = new this.google.maps.Map(
          document.getElementById("map"),
          this.options // adding options for center, map type and controls
        );

        // Adding GeoJSON 
        map.data.loadGeoJson(this.JSONurl);
        map.data.setStyle(this.JSONStyle);

        // Adding Heatmap Layer
        var heatmap = new this.google.maps.visualization.HeatmapLayer({
          data: this.heatmapPoints
        });
        heatmap.set('opacity', 0.8);
        heatmap.set('gradient', this.gradient);
        heatmap.setMap(map);

        // Customizing map with aubergine theme
        var styledMap = new this.google.maps.StyledMapType(this.mapStyle, {
          name: "Styled Map"
        });
        map.mapTypes.set("styled_map", styledMap);
        map.setMapTypeId("styled_map");
      });
    },
  },
  mounted() {this.drawMap()},
  beforeUpdate() {this.drawMap()}
};
</script>