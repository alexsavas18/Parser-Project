// Generated from alex_savas_grammar.g4 by ANTLR 4.13.2
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link alex_savas_grammarParser}.
 */
public interface alex_savas_grammarListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link alex_savas_grammarParser#prog}.
	 * @param ctx the parse tree
	 */
	void enterProg(alex_savas_grammarParser.ProgContext ctx);
	/**
	 * Exit a parse tree produced by {@link alex_savas_grammarParser#prog}.
	 * @param ctx the parse tree
	 */
	void exitProg(alex_savas_grammarParser.ProgContext ctx);
	/**
	 * Enter a parse tree produced by {@link alex_savas_grammarParser#statement}.
	 * @param ctx the parse tree
	 */
	void enterStatement(alex_savas_grammarParser.StatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link alex_savas_grammarParser#statement}.
	 * @param ctx the parse tree
	 */
	void exitStatement(alex_savas_grammarParser.StatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link alex_savas_grammarParser#assignment}.
	 * @param ctx the parse tree
	 */
	void enterAssignment(alex_savas_grammarParser.AssignmentContext ctx);
	/**
	 * Exit a parse tree produced by {@link alex_savas_grammarParser#assignment}.
	 * @param ctx the parse tree
	 */
	void exitAssignment(alex_savas_grammarParser.AssignmentContext ctx);
	/**
	 * Enter a parse tree produced by {@link alex_savas_grammarParser#arithmetic}.
	 * @param ctx the parse tree
	 */
	void enterArithmetic(alex_savas_grammarParser.ArithmeticContext ctx);
	/**
	 * Exit a parse tree produced by {@link alex_savas_grammarParser#arithmetic}.
	 * @param ctx the parse tree
	 */
	void exitArithmetic(alex_savas_grammarParser.ArithmeticContext ctx);
	/**
	 * Enter a parse tree produced by {@link alex_savas_grammarParser#arrayInit}.
	 * @param ctx the parse tree
	 */
	void enterArrayInit(alex_savas_grammarParser.ArrayInitContext ctx);
	/**
	 * Exit a parse tree produced by {@link alex_savas_grammarParser#arrayInit}.
	 * @param ctx the parse tree
	 */
	void exitArrayInit(alex_savas_grammarParser.ArrayInitContext ctx);
	/**
	 * Enter a parse tree produced by {@link alex_savas_grammarParser#boolAssign}.
	 * @param ctx the parse tree
	 */
	void enterBoolAssign(alex_savas_grammarParser.BoolAssignContext ctx);
	/**
	 * Exit a parse tree produced by {@link alex_savas_grammarParser#boolAssign}.
	 * @param ctx the parse tree
	 */
	void exitBoolAssign(alex_savas_grammarParser.BoolAssignContext ctx);
	/**
	 * Enter a parse tree produced by {@link alex_savas_grammarParser#ifBlock}.
	 * @param ctx the parse tree
	 */
	void enterIfBlock(alex_savas_grammarParser.IfBlockContext ctx);
	/**
	 * Exit a parse tree produced by {@link alex_savas_grammarParser#ifBlock}.
	 * @param ctx the parse tree
	 */
	void exitIfBlock(alex_savas_grammarParser.IfBlockContext ctx);
	/**
	 * Enter a parse tree produced by {@link alex_savas_grammarParser#conditionBlock}.
	 * @param ctx the parse tree
	 */
	void enterConditionBlock(alex_savas_grammarParser.ConditionBlockContext ctx);
	/**
	 * Exit a parse tree produced by {@link alex_savas_grammarParser#conditionBlock}.
	 * @param ctx the parse tree
	 */
	void exitConditionBlock(alex_savas_grammarParser.ConditionBlockContext ctx);
	/**
	 * Enter a parse tree produced by the {@code LogicalOperations}
	 * labeled alternative in {@link alex_savas_grammarParser#condition}.
	 * @param ctx the parse tree
	 */
	void enterLogicalOperations(alex_savas_grammarParser.LogicalOperationsContext ctx);
	/**
	 * Exit a parse tree produced by the {@code LogicalOperations}
	 * labeled alternative in {@link alex_savas_grammarParser#condition}.
	 * @param ctx the parse tree
	 */
	void exitLogicalOperations(alex_savas_grammarParser.LogicalOperationsContext ctx);
	/**
	 * Enter a parse tree produced by the {@code NotCondition}
	 * labeled alternative in {@link alex_savas_grammarParser#condition}.
	 * @param ctx the parse tree
	 */
	void enterNotCondition(alex_savas_grammarParser.NotConditionContext ctx);
	/**
	 * Exit a parse tree produced by the {@code NotCondition}
	 * labeled alternative in {@link alex_savas_grammarParser#condition}.
	 * @param ctx the parse tree
	 */
	void exitNotCondition(alex_savas_grammarParser.NotConditionContext ctx);
	/**
	 * Enter a parse tree produced by the {@code Comparison}
	 * labeled alternative in {@link alex_savas_grammarParser#condition}.
	 * @param ctx the parse tree
	 */
	void enterComparison(alex_savas_grammarParser.ComparisonContext ctx);
	/**
	 * Exit a parse tree produced by the {@code Comparison}
	 * labeled alternative in {@link alex_savas_grammarParser#condition}.
	 * @param ctx the parse tree
	 */
	void exitComparison(alex_savas_grammarParser.ComparisonContext ctx);
	/**
	 * Enter a parse tree produced by the {@code ParenCondition}
	 * labeled alternative in {@link alex_savas_grammarParser#condition}.
	 * @param ctx the parse tree
	 */
	void enterParenCondition(alex_savas_grammarParser.ParenConditionContext ctx);
	/**
	 * Exit a parse tree produced by the {@code ParenCondition}
	 * labeled alternative in {@link alex_savas_grammarParser#condition}.
	 * @param ctx the parse tree
	 */
	void exitParenCondition(alex_savas_grammarParser.ParenConditionContext ctx);
	/**
	 * Enter a parse tree produced by {@link alex_savas_grammarParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterExpr(alex_savas_grammarParser.ExprContext ctx);
	/**
	 * Exit a parse tree produced by {@link alex_savas_grammarParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitExpr(alex_savas_grammarParser.ExprContext ctx);
	/**
	 * Enter a parse tree produced by {@link alex_savas_grammarParser#comparisonOp}.
	 * @param ctx the parse tree
	 */
	void enterComparisonOp(alex_savas_grammarParser.ComparisonOpContext ctx);
	/**
	 * Exit a parse tree produced by {@link alex_savas_grammarParser#comparisonOp}.
	 * @param ctx the parse tree
	 */
	void exitComparisonOp(alex_savas_grammarParser.ComparisonOpContext ctx);
}