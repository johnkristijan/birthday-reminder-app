<template>
  <div class="about">
      App language: <b>{{ $store.state.core.language }}</b><br />
      User is logged in: <b>{{ $store.state.core.loggedIn ? 'yes' : 'no' }}</b><br />
      Current user: <b>{{ currentUser }}</b><br />

      <hr />

        
      <LanguageSelector />
      <LogInComponent />
  </div>
</template>

<script>
import LanguageSelector from './LanguageSelector'
import LogInComponent from './LogInComponent'
export default {
    name: 'About',
    components: { LanguageSelector, LogInComponent },
    computed: {
        currentUser() {
            const coreState = this.$store.state.core
            return coreState.currentUser ? coreState.currentUser : 'NA'
        }
    },
    created() {
        console.log(this.$store)
    }
}

</script>