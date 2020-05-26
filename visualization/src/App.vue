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

    <v-app-bar app  dark>
      <v-app-bar-nav-icon @click.stop="drawer = !drawer"></v-app-bar-nav-icon>
      <v-toolbar-title>Application</v-toolbar-title>
    </v-app-bar>

    <v-content>
      <v-container class="fill-height" fluid>
        <v-layout align-center justify-center>
          <Map />
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
  data: () => ({
    drawer: false
  })
};
</script>

<style>
.container{
  padding: 0;
}
</style>