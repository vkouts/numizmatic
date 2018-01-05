const ExtractTextPlugin = require ('extract-text-webpack-plugin');
const UglifyJsPlugin = require('uglifyjs-webpack-plugin')

module.exports = {
    entry: [
        './source/js/main.js',
        // './bower_components/jquery/dist/jquery.js',
        //'./bower_components/bootstrap/dist/js/bootstrap.js',
    ],
    output: {
        path: __dirname + "/dist",
        filename: 'bundle.js'
    },
    watch: true,

    watchOptions: {
        aggregateTimeout: 100
    },

    devtool: 'source-map',
    // resolve: {
    //     modulesDirectories: ['node_modules']
    // },
    module: {
        loaders: [
            // {
            //    test: /\.js/,
            //    loader: 'babel',
            //    exclude: /(node_modules|bower_components)/
            // },
            {
                test: /\.css$/,
                use: ExtractTextPlugin.extract({
				    fallback: "style-loader",
				    use: {
					    loader: "css-loader",
					    options: {
						    sourceMap: true,
                            minimize: true
					    }
				    },
				    publicPath: "../"
			    })
            },
        ]
    },
    plugins: [
        new ExtractTextPlugin('bundle.css'),
        new UglifyJsPlugin(),
        // new ProvidePlugin({
        //     $: "jquery",
        //     jQuery: "jquery",
        //     "window.jQuery": "jquery"
        // })
    ]
};