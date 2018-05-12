<template>
    <div>
    <NavHeader></NavHeader>
    <div>
      <table class="form-group">
        <tr>
          <th>Category:</th>
          <th><input type="text" class="form-control" ></th>
        </tr>
        <br>
        <tr>
          <th>标记  </th>
          <th>
            <select class="form-control" multiple="multiple" >
              <option value="1" >dasdas</option>
              <option value="1" >dasdas</option>
              <option value="1" >dasdas</option>
              <option value="1" >dasdas</option>
              <option value="1" >dasdas</option>
              <option value="1" >dasdas</option>
            </select>
          </th>
        </tr>
        <br>
        <tr>
          <th>提交</th>
          <th><button class="btn btn-danger" >submit</button></th>
        </tr>
      </table>
      <br>

    </div>
  </div>
</template>

<script>
    export default {
        name: "EditorCategory"
    }
</script>

<style scoped>

</style>
