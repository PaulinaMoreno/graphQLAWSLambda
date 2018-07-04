'use strict';

const GraphQL = require('graphql');
const {
	GraphQLList,
	GraphQLString,
	GraphQLNonNull,
} = GraphQL;

// import the Post type we created
const ContactType = require('../types/Contact');

// import the Post resolver we created
const ContactResolver = require('../resolvers/Contact');


module.exports = {

	index() {
		return {
			type: new GraphQLList(ContactType),
			description: 'This will return all the contacts we find per user',
			args: {
				contact_name: {
					type: GraphQLString,
					description: 'Please enter contact  name',
				}
			},
			resolve(parent, args, context, info) {
				return ContactResolver.index(args);
			}
		}
	},

};
