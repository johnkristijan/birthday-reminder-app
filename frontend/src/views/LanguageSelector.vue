<template>
  <div>
      <button @click="setLang('no')">Norsk</button>
      <button @click="setLang('en')">English</button>
</div>
</template>

<script>
export default {
    name: 'LanguageSelector',
    methods: {
        setLang(lang) {
            this.$store.state.core.language = lang
        }
    }
}
</script>
