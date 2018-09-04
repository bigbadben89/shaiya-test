USE [PS_GameData]
GO
/****** Object:  StoredProcedure [dbo].[usp_Check_Pet_Timer]    Script Date: 12/02/2015 16:58:45 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
/*****************************************

Author : [DEV]Lube
Name : [dbo].[usp_Check_Pet_Timer]
Description : Stored Procedure - Validate pet / costume timers
Created : 11/24/2015

*****************************************/
CREATE  Proc [dbo].[usp_Check_Pet_Timer]

@CharID int

AS

SET NOCOUNT ON

DECLARE @CreateTime datetime
DECLARE @UserUID int	
DECLARE @Cnt int
DECLARE @lCnt int
DECLARE @Timer smallint
DECLARE @ItemUID bigint

SELECT @UserUID=UserUID FROM PS_GameData.dbo.Chars WHERE CharID=@CharID

IF EXISTS(SELECT ItemUID FROM PS_GameData.dbo.CharItems WHERE [Type] IN (120,150) AND CharID=@CharID)
BEGIN	
	SELECT * INTO #TempTable FROM PS_GameData.dbo.CharItems WHERE ([Type]=120 or [Type]=150) AND CharID=@CharID
	SET @Cnt=(SELECT COUNT(ItemUID) FROM #TempTable)
	SET @lCnt=1	
	WHILE(@Cnt>@lCnt)
	BEGIN
		SET @ItemUID=(SELECT TOP 1 ItemUID FROM #TempTable)
		SET @Timer= (SELECT [Range] FROM PS_GameDefs.dbo.Items WHERE ItemID=(SELECT ItemID FROM #TempTable WHERE ItemUID=@ItemUID))
		SET @CreateTime= (SELECT Maketime FROM #TempTable WHERE ItemUID=@ItemUID)	
		IF(GETDATE() > DATEADD(DD, @Timer,@CreateTime) AND @Timer > 0)
		BEGIN
			DELETE FROM PS_GameData.dbo.CharItems WHERE CharID=@CharID AND ([Type]=120 or [Type]=150) AND ItemUID=@ItemUID
		END
		DELETE FROM #TempTable WHERE ItemUID=@ItemUID
		SET @lCnt=@lCnt+1
	END
END

IF EXISTS(SELECT ItemUID FROM PS_GameData.dbo.UserStoredItems WHERE [Type] IN (120,150) AND UserUID=@UserUID)
BEGIN	
	SELECT * INTO #TempTableWH FROM PS_GameData.dbo.UserStoredItems WHERE ([Type]=120 or [Type]=150) AND UserUID=@UserUID
	SET @Cnt=(SELECT COUNT(ItemUID) FROM #TempTableWH)
	SET @lCnt=1	
	WHILE(@Cnt>@lCnt)
	BEGIN
		SET @ItemUID=(SELECT TOP 1 ItemUID FROM #TempTableWH)
		SET @Timer= (SELECT [Range] FROM PS_GameDefs.dbo.Items WHERE ItemID=(SELECT ItemID FROM #TempTableWH WHERE ItemUID=@ItemUID))
		SET @CreateTime= (SELECT Maketime FROM #TempTableWH WHERE ItemUID=@ItemUID)	
		IF(GETDATE() > DATEADD(DD, @Timer,@CreateTime) AND @Timer > 0)
		BEGIN
			DELETE FROM PS_GameData.dbo.UserStoredItems WHERE ([Type]=120 or [Type]=150) AND UserUID=@UserUID AND ItemUID=@ItemUID
		END
		DELETE FROM #TempTableWH WHERE ItemUID=@ItemUID
		SET @lCnt=@lCnt+1
	END
END
SET NOCOUNT OFF
