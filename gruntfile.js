module.exports = function(grunt) {
	grunt.initConfig({
		pkg: grunt.file.readJSON('package.json'),

		connect: {
			server: {
				options: {
					port: 10000, 
					/*port: 8000,*/
					base: '_site'
				},
			}
		},

    jekyll: {
      build: {
        serve: false,
        incremental: true
      },
      
      options: {                          
        bundleExec: true,
        incremental: true
      },
    },

		less: {
			dev: {
				options: {
					compress: true,
				},
				files: {
					"./resources/css/pdf.css":"./resources/less/pdf.less",
					"./_site/resources/css/pdf.css":"./resources/css/pdf.css",
					"./resources/css/styles.css":"./resources/less/base.less",
					"./_site/resources/css/styles.css":"./resources/less/base.less",
					"./resources/css/slides.css":"./resources/less/slides.less",
					"./_site/resources/css/slides.css":"./resources/less/slides.less"
				}
			}
		},

		concat: {
			options: {
				separator: ';',
			},
			site: {
				src: [
					'./bower_components/jquery/dist/jquery.js',
					'./bower_components/bootstrap/dist/js/bootstrap.js',
				],
				dest: './resources/js/site.js',
			}//,
			/*slides: {
				src: [ './bower_components/reveal.js/lib/js/head.js',
					'./bower_components/reveal.js/lib/js/reveal.js',
					'./bower_components/reveal.js/plugin/zoom-js/zoom.js',
					'./bower_components/reveal.js/plugin/notes/notes.js'
				],
				dest: './resources/js/slides.js',
			}*/
		},

		copy: {
			slides: {
				nonull: true,
				expand: true,
				cwd: 'bower_components/',
				src: 'reveal.js/**',
				dest: 'resources/lib/'
			},
		},

		watch: {
			less: {
				files: ['resources/less/*.less'],
				tasks: 'less'
			},
			css: {
				files: ['resources/css/*.css'],
				tasks: 'jekyll'
			},
			jekyll: {
				files: [ 
					'*.html',
					'*.yml',
					'*.markdown',
					'slides/*/*.markdown',
					'slides/*/*.md',
					'activities/*.markdown',
					'activities/*.md',
					'assignments/*.markdown',
					'assignments/*.md',
					'code/*.*',
					'slides/*/*.html',
					'resources/js/**.js',
					'_posts/**',
					'_includes/**',
					'_layouts/**',
					'_data/*.csv',
					'!**/node_modules/**',
					'!**/_site/**',
					'!_site',
					'!_site/**',
					'!**/bower_components/**',
					'!bower.json',
					'!gruntfile.js',
					'!package.json',
					'!README.md'
							],
				options: {
					livereload: false,
					
				},
				tasks: 'jekyll',
			}
		},
	});

	grunt.registerTask('build', 'jekyll:build');
	grunt.registerTask('watch', ['watch:jekyll', 'watch:less']);
	grunt.registerTask('dev', ['concat', 'copy', 'build', 'connect', 'watch']);

	grunt.loadNpmTasks('grunt-jekyll');
	grunt.loadNpmTasks('grunt-contrib-less');
	grunt.loadNpmTasks('grunt-contrib-watch');
	grunt.loadNpmTasks('grunt-contrib-concat');
	grunt.loadNpmTasks('grunt-contrib-uglify');
	grunt.loadNpmTasks('grunt-contrib-connect');
	grunt.loadNpmTasks('grunt-contrib-copy');
};





