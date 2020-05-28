<template>
  <v-app id="inspire" dark>
    <v-navigation-drawer v-model="drawer" app dark>
      <v-list dense>
        <v-list-item>
          <v-list-item-content>
            <!-- <v-list-item-title>{{labels[tab]}}</v-list-item-title> -->
          </v-list-item-content>
        </v-list-item>
        <v-list-item>
          <v-list-item-content>
            <v-layout column>
              <v-flex v-for="category in drawerItems[tab]" :key="category">
                  <v-checkbox v-model="selectedCategories" :label="category" :value="category"></v-checkbox>
              </v-flex>
              <p>Showing results for: </p>
              <p v-for="i in selectedCategories" :key="i">{{i}}</p>
            </v-layout>
          </v-list-item-content>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>

    <v-app-bar app dark>
      <div>
        <v-tabs v-model="tab" align-with-title>
          <v-tabs-slider></v-tabs-slider>

          <v-tab v-for="item in labels" :key="item" @click="clearCategories()">{{ item }}</v-tab>
        </v-tabs>
      </div>
    </v-app-bar>
    <v-content>
      <v-container class="fill-height" fluid>
        <v-layout align-center justify-center column>
          <Map :points="points[tab]" />
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
import { db } from "./firebase/init.js";
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
      drawer: true,
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
      drawerItems: [
        ["0-18", "19-25", "26-45", "45-65", "65-80", "Above 80"],
        ["white", "hispanic", "black", "asian", "other"]
      ],
      selectedCategories: []
      // currentPoints: this.points[this.tab]
    };
  },
  methods:{
    clearCategories: function(){
      this.selectedCategories = []
    }
  },
  mounted() {
    console.log("In mounted");
    db.collection("test")
      .get()
      .then(function(querySnapshot) {
        querySnapshot.forEach(function(doc) {
          console.log(doc.id, " => ", doc.data());
        });
      });
    // db.collection("test")
    //   .doc("person 7")
    //   .set({
    //     age: 15,
    //     contact: true,
    //     location: "02135",
    //     race: "asian",
    //     severity: "severe"
    //   });
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