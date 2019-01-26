module.exports = {
  productionSourceMap: false, // 生产环境的 source map
  configureWebpack: {
    performance: {
      hints: false
    },
    optimization: {
      splitChunks: {
        minSize: 10000,
        maxSize: 250000
      }
    }
  }
}
