<template>
  <div>
    <!--<NavHeader></NavHeader>-->
    <!-- article -->
    <h1>
      <router-link :to="{path: '/new_article'}">Article</router-link>
    </h1>
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
        <td>
          <template v-for="t in article.tags">
            {{t}}
          </template>
        </td>
        <td>{{article.date}}</td>
        <td>
          <router-link :to="{path: '/article/' + article.date + '/' + article.slug + '/editor'}">edit</router-link>
          <a href="" @click="article_delete(article.id)">delete</a>
        </td>
      </tr>
      </tbody>
    </table>
    <!-- ################################################ -->
    <!-- category-->
    <h1>
      <router-link :to="{path: '/new_category'}">Category</router-link>
    </h1>
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
        <td>
          <router-link :to="{path: '/manage' + '/category/' + category.name + '/editor'}">edit</router-link>
          <a @click="category_delete(category.id)">delete</a></td>
      </tr>
      </tbody>
    </table>
    <!-- ################################################ -->
    <!-- tag -->
    <h1>
      <router-link :to="{path: '/new_tag'}">Tag</router-link>
    </h1>
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
      <tr v-for="tag in manage.tags">
        <th scope="row">{{tag.id}}</th>
        <td>{{tag.name}}</td>
        <td>{{tag.date}}</td>
        <td>
          <router-link :to="{path: '/manage' + '/tag/' + tag.name + '/editor'}">edit</router-link>
          <a href="" @click="tag_delete(tag.id)">delete</a></td>
      </tr>
      </tbody>
    </table>
    <!-- ################################################ -->
  </div>
</template>

<script>
  import NavHeader from '@/components/index/NavHeader'

  export default {
    name: "Manage",
    components: {NavHeader},
    data() {
      return {
        manage: []
      }
    },
    mounted() {
      this.$axios.get('https://buglan.org/api/manage', {headers: {'Authorization': 'Bearer '+ this.getCookie('token')}})
        .then(response => {
          this.manage = response.data.manage;
          document.title = 'Manage | BUGLAN';
        })
    },
    methods: {
      article_delete: function (id) {
        this.$axios.delete('https://buglan.org/api/article_operation', {params: {'id': id}}, {headers: {'Authorization': 'Bearer '+ this.getCookie('token')}})
          .then(response => {
            if (response.status === 200) {
              alert('删除成功')
              this.$router.go(0)
            }
          })
      },
      category_delete: function (id) {
        this.$axios.delete('https://buglan.org/api/category_operation', {params: {'id': id}}, {headers: {'Authorization': 'Bearer '+ this.getCookie('token')}})
          .then(response => {
            if (response.status === 200) {
              alert('删除成功')
              this.$router.go(0)
            }
          })
      },
      tag_delete: function (id) {
        this.$axios.delete('https://buglan.org/api/tag_operation', {params: {'id': id}}, {headers: {'Authorization': 'Bearer '+ this.getCookie('token')}})
          .then(response => {
            if (response.status === 200) {
              alert('删除成功')
              this.$router.go(0)
            }
          })
      }
    },
    /*watch: {
      '$route'(to, from) {
        this.$axios.get('http://127.0.0.1:5000/api/manage')
          .then(response => {
            this.manage = response.data.manage;
          })
      }
    }*/
  }
</script>

<style scoped>

</style>
