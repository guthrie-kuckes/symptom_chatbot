<template>
  <v-app id="inspire" dark>
    <v-navigation-drawer  hide-overlay permanent app dark>
      <v-list dense>
        <v-list-item>
          <v-list-item-content>
            <!-- <v-list-item-title>{{labels[tab]}}</v-list-item-title> -->
          </v-list-item-content>
        </v-list-item>
        <v-list-item>
          <v-list-item-content>
            <v-layout column>
              <v-select 
              v-model='tabItem' 
              :items='labels'  
              label="Category"
              :item-text="tabItem" 
              outlined
              @click=clearCategories()
              ></v-select>
              <v-flex v-for="category in drawerItems[tabItem]" :key="category.substring(0,2)">
                <v-checkbox v-model="selectedCategories" :label="category" :value="category"></v-checkbox>
              </v-flex>
              <v-btn @click="search(selectedCategories)">Search</v-btn>
              <p>Showing results for:</p>
              <p v-for="i in selectedCategories" :key="i">{{i}}</p>
            </v-layout>
          </v-list-item-content>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>

    <v-app-bar app dark>
      <!-- <v-app-bar-nav-icon @click.stop="drawer = !drawer"></v-app-bar-nav-icon> -->
      <div>
        <!-- <v-tabs v-model="tab" align-with-title>
          <v-tabs-slider></v-tabs-slider>

          <v-tab v-for="item in labels" :key="item" @click="clearCategories()">{{ item }}</v-tab>
        </v-tabs> -->
      </div>
    </v-app-bar>
    <v-content>
      <v-container class="fill-height" fluid>
        <v-layout align-center justify-center column>
        <Map v-if="result == 0" :points="points" />
        <p v-else-if="result == 1">Loading</p>
        <p v-else>No results </p>
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
import firebase from "firebase/app";
import "@firebase/functions";

export default {
  components: {
    Map
  },
  props: {
    source: String
  },
  // ini
  data() {
    return {
      result: 0,
      tabItem: '',
      tab: 0,
      drawer: true,
      active: null,
      labels: ["Age", "Race", "Symptom Severity", "Contact", "Gender"],
      points: [
        { lat: 42.35843, lng: -71.05977 },
        { lat: 42.357117, lng: -71.059719 },
        { lat: 42.356117, lng: -71.059719 },
        { lat: 42.354117, lng: -71.058719 },
        { lat: 42.356117, lng: -71.059919 },
        { lat: 42.356117, lng: -71.059019 },
        { lat: 42.356117, lng: -71.059719 },
        { lat: 42.25843, lng: -71.05977 },
        { lat: 42.257117, lng: -71.059719 },
        { lat: 42.256117, lng: -71.059719 },
        { lat: 42.254117, lng: -71.058719 },
        { lat: 42.256117, lng: -71.059919 },
        { lat: 42.256117, lng: -71.059019 },
        { lat: 42.256117, lng: -71.059719 }
      ],
      drawerItems: {
        "": null,
        "Age": ["0-18", "19-25", "26-45", "45-65", "65-80", "Above 80"],
        "Race": ["white", "hispanic", "black", "asian", "other"],
        "Symptom Severity": ["none", "mild", "moderate", "severe"],
        "Contact":["Yes", "No"],
        "Gender": ["female", "male", "other"]
      },
      selectedCategories: []
      // currentPoints: this.points[this.tab]
    };
  },
  methods: {
    clearCategories: function() {
      this.selectedCategories = [];
    },
    search: function(params) {
      this.result = 1

      params.forEach(function(item) {
        console.log(item);
      });

      var cors_enabled = firebase.functions().httpsCallable("cors_enabled");

      var _selectedRace = this.tab == 0 ? this.selectedCategories : [];
      var _selectedAge = this.tab == 1 ? this.selectedCategories : [];
      var _selectedSymptoms = this.tab == 2 ? this.selectedCategories : [];
      var _selectedContact =
        this.tab == 3 ? this.intoBoolean(this.selectedCategories) : [];
      // var _selectedGender = this.tab == 4 ? this.selectedCategories : [];


      // console.log("result is", _selectedContact);

      params = {
        race: _selectedRace,
        age: _selectedAge,
        severity: _selectedSymptoms,
        contact: _selectedContact,
        // gender: _selectedGender
      };
      // params = {race: ["white", "hispanic"]};

      console.log("params is", params);
      cors_enabled(params).then(
        res => {
          console.log(res)
          res.data.forEach(function(item) {
            console.log(item);
          });
          if (res.data.length > 0) {
            this.points = res.data;
            this.result = 0
          } else{
            console.log("NO results")
            this.result = 2
          }
        },
        error => {
          console.log("Error is", error);
        }
      );
    },
    intoBoolean: function(cat) {
      var res = [];
      for (var item in cat) {
        if (item == "yes") {
          res.push(true);
        } else {
          res.push(false);
        }
      }
      return res;
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