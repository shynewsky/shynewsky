#ifndef _CRT_SECURE_NO_WARNINGS
#define _CRT_SECURE_NO_WARNINGS
#endif

#include <stdio.h>

#define CATEGORY_NUM	3

#define CMD_INIT        100
#define CMD_SOW			200
#define CMD_WATER    	300
#define CMD_HARVEST    	400

extern void init(int N, int mGrowthTime[]);
extern int sow(int mTime, int mRow, int mCol, int mCategory);
extern int water(int mTime, int G, int mRow, int mCol, int mHeight, int mWidth);
extern int harvest(int mTime, int L, int mRow, int mCol, int mHeight, int mWidth);

static bool run()
{
	int Q, ret, ans;
	int N, mGrowthTime[CATEGORY_NUM], mTime, mCategory, L, G, mRow, mCol, mHeight, mWidth;

	scanf("%d", &Q);
	bool okay = false;

	for (int q = 0; q < Q; ++q)
	{
		int cmd;
		scanf("%d", &cmd);
		switch (cmd) {
		case CMD_INIT:
			scanf("%d %d %d %d", &N, &mGrowthTime[0], &mGrowthTime[1], &mGrowthTime[2]);
			init(N, mGrowthTime);
			okay = true;
			break;
		case CMD_SOW:
			scanf("%d %d %d %d %d", &mTime, &mRow, &mCol, &mCategory, &ans);
			ret = sow(mTime, mRow, mCol, mCategory);
			if (ans != ret)
				okay = false;
			break;
		case CMD_WATER:
			scanf("%d %d %d %d %d %d %d", &mTime, &G, &mRow, &mCol, &mHeight, &mWidth, &ans);
			ret = water(mTime, G, mRow, mCol, mHeight, mWidth);
			if (ans != ret)
				okay = false;
			break;
		case CMD_HARVEST:
			scanf("%d %d %d %d %d %d %d", &mTime, &L, &mRow, &mCol, &mHeight, &mWidth, &ans);
			ret = harvest(mTime, L, mRow, mCol, mHeight, mWidth);
			if (ans != ret)
				okay = false;
			break;
		default:
			okay = false;
			break;
		}
	}

	return okay;
}

int main()
{
	setbuf(stdout, NULL);
	// freopen("sample_input.txt", "r", stdin);

	int TC, MARK;

	scanf("%d %d", &TC, &MARK);
	for (int tc = 1; tc <= TC; ++tc)
	{
		int score = run() ? MARK : 0;
		printf("#%d %d\n", tc, score);
	}

	return 0;
}