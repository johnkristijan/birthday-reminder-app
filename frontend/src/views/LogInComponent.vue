<template>
  <div>
      <input v-if="!isLoggedIn" type="text" v-model="username" placeholder="Username" />
      <button v-if="!isLoggedIn" @click="login">Log in</button>
      <button v-else @click="logout">Log out</button>
  </div>
</template>

<script>
export default {
    name: 'LogInComponent',
    data() {
        return {
            username: null
        }
    },
    computed: {
        isLoggedIn() {
            return this.$store.state.core.loggedIn
        }
    },
    methods: {
        login() {
            // validation!!
            this.$store.state.core.currentUser = this.username
            this.$store.state.core.loggedIn = true
        },
        logout() {
            this.$store.state.core.currentUser = null
            this.$store.state.core.loggedIn = false
        }
    }
}
</script>