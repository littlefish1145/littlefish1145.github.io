export type FriendLink = {
	name: string;
	url: string;
	kind: 'github' | 'bilibili' | 'project';
	github?: string;
	bilibili?: string;
	type?: 'github' | 'bilibili';
	avatar?: string;
	description?: string;
	tags?: string[];
	status?: 'active' | 'inactive';
};

export const links: FriendLink[] = [
	{
		name: 'Amira',
		kind: 'github',
		github: 'littlefish1145',
		url: 'https://github.com/littlefish1145',
		bilibili: 'https://space.bilibili.com/3546573311051825',
		description:
			'来杯好茶摇一摇,This is me!!!!',
		tags: ['Blog', 'Tech'],
		status: 'active',
	},
];
