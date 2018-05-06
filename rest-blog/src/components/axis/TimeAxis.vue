<template>
  <div>
    <div v-for="item in items">
      <h2>{{item.name}}</h2>
      <ul v-for="title in item.titles">
        <li>{{title.date}} => {{title.name}}</li>
      </ul>
    </div>
  </div>
</template>

<script>
  // 获取所有标签
  export default {
    name: "TimeAxis",
    data(){
      return {
        items: ''
      }
    },
    mounted() {
      this.$axios.get('http://127.0.0.1:5000/api/categories')
        .then(response => {
          this.items = response.data['category_json']
        })
    }
  }
</script>

<style scoped>

</style>
