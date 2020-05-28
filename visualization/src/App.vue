<template>
  <v-app id="inspire" dark>
    <v-navigation-drawer v-model="drawer" app dark>
      <v-list dense>
        <v-list-item link>
          <v-list-item-action>
            <v-icon>mdi-home</v-icon>
          </v-list-item-action>
          <v-list-item-content>
            <v-list-item-title>Home</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
        <v-list-item link>
          <v-list-item-action>
            <v-icon>mdi-contact-mail</v-icon>
          </v-list-item-action>
          <v-list-item-content>
            <v-list-item-title>Contact</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>

    <v-app-bar app dark>
      <div>
        <v-tabs v-model="tab" align-with-title>
          <v-tabs-slider ></v-tabs-slider>

          <v-tab v-for="item in labels" :key="item">{{ item }}</v-tab>
        </v-tabs>
      </div>
    </v-app-bar>
    <v-content>
      <v-container class="fill-height" fluid>
        <v-layout align-center justify-center column>
          <Map :points="points[tab]"/>
          
        </v-layout>
      </v-container>
    </v-content>
    <v-footer dark app>
      <span class="white--text">&copy; 2020</span>
    </v-footer>
  </v-app>
</template>

<script>
import Map from "./components/Map.vue";
export default {
  components: {
    Map
  },
  props: {
    source: String
  },
  data() {
    return {
      tab: 0,
      drawer: false,
      active: null,
      labels: ["Age", "Race"],
      points: [
        [
          { lat: 42.35843, lng: -71.05977 },
          { lat: 42.357117, lng: -71.059719 },
          { lat: 42.356117, lng: -71.059719 },
          { lat: 42.354117, lng: -71.058719 },
          { lat: 42.356117, lng: -71.059919 },
          { lat: 42.356117, lng: -71.059019 },
          { lat: 42.356117, lng: -71.059719 }
        ],
        [
          { lat: 42.25843, lng: -71.05977 },
          { lat: 42.257117, lng: -71.059719 },
          { lat: 42.256117, lng: -71.059719 },
          { lat: 42.254117, lng: -71.058719 },
          { lat: 42.256117, lng: -71.059919 },
          { lat: 42.256117, lng: -71.059019 },
          { lat: 42.256117, lng: -71.059719 }
        ]
      ],
      // currentPoints: this.points[this.tab]
    };
  }
};
</script>

<style>
.container {
  padding: 0;
}

.v-window-item.v-window-item--active,
.v-window.v-item-group.theme--light.v-tabs-items {
  height: 100%;
  width: 100%;
}
</style>