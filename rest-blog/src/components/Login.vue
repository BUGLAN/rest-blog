<template>
  <div>
    <NavHeader></NavHeader>
    <div>
      <table class="form-group">
        <tr>
          <th>Username:</th>
          <th><input type="text" class="form-control"></th>
        </tr>
        <br>
        <tr>
          <th>Password:</th>
          <th><input type="password" class="form-control"></th>
        </tr>
        <br>
        <tr>
          <th>Submit:</th>
          <th>
            <button class="btn btn-danger" >submit</button>
          </th>
        </tr>
      </table>
    </div>
  </div>

</template>

<script>
  import NavHeader from '@/components/index/NavHeader'

  export default {
    name: "Login",
    components: {NavHeader}
  }
</script>

<style scoped>

</style>
