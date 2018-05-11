<template>
  <div>
    <NavHeader></NavHeader>
    <h1><a href="">Category</a></h1>
    <table class="table">
      <thead>
      <tr>
        <th>#</th>
        <th>Name</th>
        <th>Date</th>
        <th>Operation</th>
      </tr>
      </thead>
      <tbody>
      <tr v-for="category in manage['categories']">
        <th scope="row">{{category.id}}</th>
        <td>{{category.name}}</td>
        <td>{{category.date}}</td>
        <td><a href="">edit</a></td>
      </tr>
      </tbody>
    </table>
    <!-- ################################################ -->
    <h1><a href="">Tag</a></h1>
    <table class="table">
      <thead>
      <tr>
        <th>#</th>
        <th>Name</th>
        <th>Time</th>
        <th>Operation</th>
      </tr>
      </thead>
      <tbody>
      <tr>
        <th scope="row">1</th>
        <td>Mark</td>
        <td>Otto</td>
        <td><a href="">edit</a></td>
      </tr>
      <tr>
        <th scope="row">2</th>
        <td>Jacob</td>
        <td>Thornton</td>
        <td><a href="">edit</a></td>
      </tr>
      <tr>
        <th scope="row">3</th>
        <td>Larry</td>
        <td>the Bird</td>
        <td><a href="">edit</a></td>
      </tr>
      </tbody>
    </table>
    <!-- ################################################ -->
    <h1><a href="">Post</a></h1>
    <table class="table">
      <thead>
      <tr>
        <th>#</th>
        <th>Post</th>
        <th>Category</th>
        <th>Tags</th>
        <th>Date</th>
        <th>Operation</th>
      </tr>
      </thead>
      <tbody>
      <tr v-for="article in manage.articles">
        <th scope="row">{{article.id}}</th>
        <td>{{article.title}}</td>
        <td>{{article.category}}</td>
        <td>@mdo</td>
        <td>{{article.date}}</td>
        <td><router-link :to="{path: '/article/' + article.date + '/' + article.title}">edit</router-link></td>
      </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
  import NavHeader from '@/components/index/NavHeader'

  export default {
    name: "Manage",
    components: {NavHeader},
    data(){
      return {
        manage: []
      }
    },
    mounted(){
      this.$axios.get('http://127.0.0.1:5000/api/manage')
        .then(response => {
          this.manage = response.data.manage;
        })
    }
  }
</script>

<style scoped>

</style>
