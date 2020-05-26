import Vue from 'vue'
import App from './App.vue'
import VueGoogleHeatmap from 'vue-google-heatmap';
import vuetify from './plugins/vuetify';

Vue.use(VueGoogleHeatmap, {
  apiKey: "AIzaSyBoPENiji-slQ3gjdjEY1WRKOfNgatSpMU"
});

Vue.config.productionTip = false

new Vue({
  vuetify,
  render: h => h(App)
}).$mount('#app')
