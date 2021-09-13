<template>
  <div id="app">
    <div id="nav">
      <NavBar />
      <!-- <router-link to="/">Home</router-link> | -->
      <!-- <router-link to="/about">About</router-link> -->
    </div>
    <router-view />
  </div>
</template>

<script>
import NavBar from "./components/NavBar";
export default {
  name: "App",
  data() {
    return {
      birthdayList: [
        { id: 1, name: "John", birthDate: "24.12.87", age: 33 },
        { id: 2, name: "Arne", birthDate: "24.12.87", age: 44 },
        { id: 3, name: "Bjarne", birthDate: "24.12.87", age: 12 },
        { id: 4, name: "Bernt", birthDate: "24.12.87", age: 8 },
        { id: 5, name: "Berit", birthDate: "24.12.87", age: 5 },
      ],
    };
  },
  components: {
    NavBar,
  },
};
</script>
