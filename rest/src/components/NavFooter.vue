<template>
  <nav>
    <h1>
      <router-link v-for="page in pages" :key="page" :to="{path: '/', query: {page: page}}" >{{page}} </router-link>
    </h1>
  </nav>
</template>

<script>
export default {
  name: 'NavFooter',
  data () {
    return {
      pages: []
    }
  },
  mounted () {
    this.$axios.get('/api/pages')
      .then(response => {
        this.pages = response.data['pages']
      })
  }
}
</script>

<style scoped>

</style>
